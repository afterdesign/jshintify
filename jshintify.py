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

        run_jshint(view, ERRORS, SETTINGS)

    def on_load(self, view):#pylint: disable-msg=R0201
        """
        Event triggered after file open
        """

        run_jshint(view, ERRORS, SETTINGS)

    def on_selection_modified(self, view):#pylint: disable-msg=R0201
        """
        Event triggered during moving in editor
        """
        (js_file_name, js_file_name_hash) = get_file_information(view)
        
        try:
            check_file_extension(js_file_name, SETTINGS)
        except Error:
            return

        row = view.rowcol(view.sel()[0].begin())[0]
        
        if str(row + 1) in ERRORS[js_file_name_hash]:
            this_error = ERRORS[js_file_name_hash][str(row + 1)]
            string = "{id} : {reason}".format(
                id = this_error['id'],
                reason = this_error['reason']
                )

            view.set_status("JSHint", string)

        elif view.get_status("JSHint"):
            view.erase_status("JSHint")


def get_file_information(view):
    """
    Get current filename
    """

    if view.file_name() is not None:
        return (view.file_name(), sha1(view.file_name()).hexdigest())
    elif view.window() is not None and view.window().active_view().file_name() is not None:
        return (view.window().active_view().file_name(), sha1(view.window().active_view().file_name()).hexdigest())
    else:
        raise Error("This may be a bug, please create issue on github")

def check_file_extension(js_file_name, settings):
    """
    Check if file should be linted or not.
    """

    file_extensions = settings.get("extensions") or []

    if os.path.splitext(js_file_name)[1] not in file_extensions:
        raise Error("File not on list")

    return True

def create_command(settings, js_file_name):
    """
    Create command list
    """

    command = []
    platform = sublime.platform()
    if platform not in settings.get('paths') or len(settings.get('paths')[platform]['node_path']) == 0 or \
        len(settings.get('paths')[platform]['jshint_path']) == 0:
        print "SET PATHS FOR NODE AND JSHINT FOR YOUR PLATFORM"

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
    
    (js_file_name, js_file_name_hash) = get_file_information(view)

    try:
        check_file_extension(js_file_name, settings)
    except Error:
        return

    if js_file_name_hash not in errors:
        errors[js_file_name_hash] = {}

    command = create_command(settings, js_file_name)
    proc = subprocess.Popen(command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    (out, err) = proc.communicate()

    if type(err) == bytes and len(err) > 0:
        raise Error(err)

    new_errors = json.loads(out)

    for line in errors[js_file_name_hash]:
        if line not in new_errors:
            draw_line(view, line, sublime.DRAW_EMPTY_AS_OVERWRITE, settings)
            view.erase_regions('jshintify.error.' + line)
        else:
            del new_errors[line]

    for line in new_errors:
        draw_line(view, line, sublime.DRAW_OUTLINED, settings)
    
    if len(new_errors) == 0:
        errors[js_file_name_hash] = {}
    else:
        errors[js_file_name_hash].update(new_errors)

def draw_line(view, line_number, draw_type, settings):
    """
    Draw outline/"dot".
    """
    dot_sign = ''
    if settings.get('show')['dot'] and draw_type != sublime.DRAW_EMPTY_AS_OVERWRITE:
        dot_sign = 'dot'

    if not settings.get('show')['outline']:
        draw_type = sublime.DRAW_EMPTY_AS_OVERWRITE


    line = view.line(view.text_point(int(line_number) - 1, 0))
    view.add_regions('jshintify.error.' + line_number, [line],
                    'jshintify.error.' + line_number, dot_sign, draw_type)

class Error(Exception):
    """
    Just generic error for module
    """
    pass