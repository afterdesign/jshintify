[![endorse](https://api.coderwall.com/afterdesign/endorsecount.png)](https://coderwall.com/afterdesign)

# yet another jshint plugin for sublime

# How to install ?
## OSX:

1. install [nodejs >= 0.8](http://nodejs.org/download/) ```brew install nodejs``` - this will take a while
2. preferably add ```/usr/local/share/npm/bin``` to $PATH
3. install [jshint](http://www.jshint.com/) ```npm install jshint -g```
4. install jshintify sublime package from git (or just use [package control](https://sublime.wbond.net/)):

    ```
    cd $PATH_OF_SUBLIME_PACKAGES (probably somethint like cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/)
    git clone git://github.com/afterdesign/jshintify.git
    ```
5. open preferences and check if the paths for node and jshint are correct
6. set the path to your jshint file
7. use ```ctrl+super+j``` to run manually
8. use ``` ctrl+shift+j``` to show list of errors in current line

## Windows:

1. install [nodejs >= 0.8](http://nodejs.org/download/)
2. install [git](http://git-scm.com/)
3. open ```node.js command prompt``` and install [jshint](http://www.jshint.com/):

    ```
    npm install jshint -g
    ```
4. open ```git Bash prompt``` and do something similar to (or just use [package control](https://sublime.wbond.net/)):

    ```
    cd $PATH_OF_SUBLIME_PACKAGES (probably something like /c/Document\ And\ Settings/YOUR_USER/Application\ Data/Sublime\ Text\ 2/Packages/)
    git clone git://github.com/afterdesign/jshintify.git
    ```
5. check ```jshint_path``` cause it's set up to ```jshint.cmd``` and it may require to find that file and set whole path like:

    ```
    C:\\Documents And Settings'\IEUser\\Application Data\\npm\\jshint.cmd
    ```

6. set the path to your jshint file
7. use ```ctrl+super+j``` to run manually
8. use ``` ctrl+shift+j``` to show list of errors in current line

## Linux:

1. Install [nodejs >= 0.8](http://nodejs.org/download/). Preferably with package manager.
2. install [jshint](http://www.jshint.com/) ```npm install jshint -g```
3. install jshintify sublime package ((or just use [package control](https://sublime.wbond.net/))):

    ```
    cd $PATH_OF_SUBLIME_PACKAGES (probably somethint like cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/)
    git clone git://github.com/afterdesign/jshintify.git
    ```
4. open preferences and check if the paths for node and jshint are correct
5. set the path to your jshint file
6. use ```ctrl+super+j``` to run manually
7. use ``` ctrl+shift+j``` to show list of errors in current line

## Pure download version:
1. Download [nodejs >= 0.8](http://nodejs.org/download/) binary.
2. Unpack
3. Open terminal or whatever you need and go to ```node-v0.10.12-linux-x64/bin```
4. install jshint ```./npm install jshint -g```
5. Configure paths in sublime jshintify plugin.

# Default settings:

1. ```run_on_load``` - run jshint right after file is loaded do editor
2. ```run_on_save``` - run jshint after file is saved
3. ```error_messages_show_count``` and ```error_messages_show_first```
    ```error_messages_show_count : false``` show message like:

    ```
    (error) : Expected 'for' to have an indentation at 13 instead at 9.
    ```

    ```"error_messages_show_count" : true``` show message like:

    ```
    ERRORS : 1 | (error) : Expected 'for' to have an indentation at 13 instead at 9.
    ```
4. ```show_dot``` - show dot on panel with line number
5. ```show_outline``` - draw outline on line with error
6. ```debug``` - use to get info to post in github issue

```
{
    "debug" : false,

    "run_on_load" : false,
    "run_on_save" : true,

    "error_messages_show_count" : true,
    "error_messages_show_first" : true,

    "extensions" : [".js"],
    "jshintrc" : "",

    "show_dot" : true,
    "show_outline" : true,

    "paths" : {
        "osx" : {
            "jshint_path" : "/usr/local/bin/jshint",
            "node_path" : "/usr/local/bin/node"
        },
        "windows" : {
            "jshint_path" : "jshint.cmd",
            "node_path" : null
        },
        "linux" : {
            "jshint_path" : "/usr/bin/jshint",
            "node_path" : "/usr/bin/node"
        }
    }
}
```

# Contact

You can follow me on twitter: [@afterdesign](http://twitter.com/afterdesign)
or find me on coderwall: [@afterdesign](http://coderwall.com/afterdesign)
or find me on g+: [+RafałMalinowski](https://plus.google.com/+Rafa%C5%82Malinowski/posts)

# License

Licensed under the [MIT license](http://opensource.org/licenses/MIT).
