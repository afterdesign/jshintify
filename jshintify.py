# -*- coding: utf-8 -*-
'''
Sublime text plugin that opens terminal.
'''

import sublime_plugin
import os
import sublime
import subprocess
import json
from hashlib import sha1

SETTINGS = sublime.load_settings('Jshintify.sublime-settings')

RUN_ON_LOAD = SETTINGS.get('run_on_load', False)
RUN_ON_SAVE = SETTINGS.get('run_on_save', False)

ERRORS_SHOW_COUNT = SETTINGS.get('error_messages_show_count', False)
ERRORS_SHOW_FIRST = SETTINGS.get('error_messages_show_first', False)

EXTENSIONS = SETTINGS.get('extensions', [])

SHOW_DOT = SETTINGS.get('show_dot', False)
SHOW_OUTLINE = SETTINGS.get('show_outline', False)

# for now let's cache those errors
ERRORS = {}

class Jshintify(sublime_plugin.TextCommand):#pylint: disable-msg=R0903,W0232
    '''
    Run jshint from sublime with configured shortcut
    '''

    def run(self, edit):#pylint: disable-msg=R0903,W0232,W0613
        '''
        Sublime text runs this

        @param edit: sublime.Edit
        '''
        run_jshint(self.view, ERRORS, SETTINGS)

class JslintifyEventListener(sublime_plugin.EventListener):#pylint: disable-msg=R0903,W0232,W0613
    """
    Class for event listeners
    """

    def on_post_save(self, view):#pylint: disable-msg=R0201
        """
        Event triggered after file save
        """
        if RUN_ON_SAVE:
            run_jshint(view, ERRORS, SETTINGS)

    def on_load(self, view):#pylint: disable-msg=R0201
        """
        Event triggered after file open
        """
        if RUN_ON_LOAD:
            run_jshint(view, ERRORS, SETTINGS)

    def on_selection_modified(self, view):#pylint: disable-msg=R0201
        """
        Event triggered during moving in editor
        """
        try:
            js_file_name_hash = check_file(view)[1]
        except Error:
            return

        row = view.rowcol(view.sel()[0].begin())[0]

        if js_file_name_hash in ERRORS and str(row + 1) in ERRORS[js_file_name_hash]:
            this_error = ERRORS[js_file_name_hash][str(row + 1)][0]

            string = ''
            if ERRORS_SHOW_COUNT:
                string += "ERRORS : {count} | ".format(count = len(ERRORS[js_file_name_hash][str(row + 1)]))

            if ERRORS_SHOW_FIRST:
                string += get_error_string(this_error)

            view.set_status("JSHint", string)

        elif view.get_status("JSHint"):
            view.erase_status("JSHint")

class JshintifyQuickPanelCommand(sublime_plugin.TextCommand):#pylint: disable-msg=R0903,W0232
    """Command to clear the sniffer marks from the view"""
    description = 'Clear sniffer marks...'

    def run(self, edit):#pylint: disable-msg=R0903,W0232,W0613
        """
        Run plugin
        """
        row = self.view.rowcol(self.view.sel()[0].begin())[0]

        try:
            js_file_name_hash = check_file(self.view)[1]
        except Error:
            return

        if js_file_name_hash in ERRORS and str(row + 1) in ERRORS[js_file_name_hash]:
            error_data = []
            for error in ERRORS[js_file_name_hash][str(row + 1)]:
                error_data.append(get_error_string(error))

            self.view.window().show_quick_panel(error_data, None, sublime.MONOSPACE_FONT)

def check_file(view):
    """
    Get current filename
    """

    if view.file_name() is not None:
        js_file_name = view.file_name()
    elif view.window() is not None and view.window().active_view().file_name() is not None:
        js_file_name = view.window().active_view().file_name()
    else:
        raise Error("This may be a bug, please create issue on github")

    if os.path.splitext(js_file_name)[1] not in EXTENSIONS:
        raise Error("File not on list")

    return (js_file_name, sha1(js_file_name).hexdigest())


def create_command(settings, js_file_name):
    """
    Create command list
    """

    command = []
    platform = sublime.platform()
    if platform not in settings.get('paths') or len(settings.get('paths')[platform]['node_path']) == 0 or \
        len(settings.get('paths')[platform]['jshint_path']) == 0:
        print("SET PATHS FOR NODE AND JSHINT FOR YOUR PLATFORM")

        return False

    command.append(settings.get('paths')[platform]['node_path'])
    command.append(settings.get("paths")[platform]['jshint_path'])
    
    command.append("--reporter")
    reporter_path = "{packages_dir}/jshintify/json-reporter.js".format(
            packages_dir = sublime.packages_path()
        )
    command.append(reporter_path)

    if len(settings.get("jshintrc")) > 0:
        command.append("--config")
        command.append(settings.get("jshintrc"))

    command.append(js_file_name)

    return command

def run_jshint(view, errors, settings):
    """
    Run jshint
    """
    
    try:
        (js_file_name, js_file_name_hash) = check_file(view)
    except Error:
        return

    if js_file_name_hash not in errors:
        errors[js_file_name_hash] = {}

    command = create_command(settings, js_file_name)
    if command == False:
        return

    proc = subprocess.Popen(command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    (out, err) = proc.communicate()

    if type(err) == bytes and len(err) > 0:
        raise Error(err)

    new_errors = json.loads(out)

    for line in errors[js_file_name_hash]:
        if line not in new_errors:
            draw_line(view, line, sublime.DRAW_EMPTY_AS_OVERWRITE)
            view.erase_regions('jshintify.error')
        else:
            del new_errors[line]

    for line in new_errors:
        draw_line(view, line, sublime.DRAW_OUTLINED)
    
    if len(new_errors) == 0:
        errors[js_file_name_hash] = {}
    else:
        errors[js_file_name_hash].update(new_errors)

def draw_line(view, line_number, draw_type):
    """
    Draw outline/"dot".
    """
    dot_sign = ''
    if SHOW_DOT and draw_type != sublime.DRAW_EMPTY_AS_OVERWRITE:
        dot_sign = 'dot'

    if not SHOW_OUTLINE:
        draw_type = sublime.DRAW_EMPTY_AS_OVERWRITE

    line = view.line(view.text_point(int(line_number) - 1, 0))
    view.add_regions('jshintify.error.' + line_number, [line],
                    'jshintify.error', dot_sign, draw_type)

def get_error_string(error):
    """
    Return Error string
    """

    return "{id} : {reason}".format(id = error['id'], reason = error['reason'])

class Error(Exception):
    """
    Just generic error for module
    """
    pass