# yet another jshint plugin for sublime

# How to install ?
## OSX:

1. ```brew install nodejs``` - this will take while
2. add ```/usr/local/share/npm/bin``` to $PATH or 
3. ```npm install jshint -g```
4. install jshintify sublime package (for now only git):

    ```
    cd $PATH_OF_SUBLIME_PACKAGES (probably somethint like cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/)
    git clone git://github.com/afterdesign/jshintify.git
    ```
5. open preferences and check if the paths for node and jshint are correct
6. set the path to your jshint file
7. use ```ctrl+super+j``` to run
8. use ``` ctrl+shift+j``` to show list of errors in current line

## Windows:
1. Install [nodejs](http://nodejs.org/download/)
2. Install [git](http://git-scm.com/)
3. Open ```node.js command prompt``` and type:

	```
	npm install jshint -g
	```
4. Open ```git Bash prompt``` and do something similar to:

	```
	cd $PATH_OF_SUBLIME_PACKAGES (probably something like /c/Document\ And\ Settings/YOUR_USER/Application\ Data/Sublime\ Text\ 2/Packages/)
	git clone git://github.com/afterdesign/jshintify.git
	```
5. Check ```jshint_path``` cause it's set up to ```jshint.cmd``` and it may require to find that file and set whole path like:
	
	```
	C:\\Documents And Settings'\IEUser\\Application Data\\npm\\jshint.cmd
	```

6. Open sublime and configure jshint with some awesome [jshitrc](http://www.jshint.com/docs/#usage) file


## Default settings:

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


```
{
    "run_on_load" : false,
    "run_on_save" : true,

    "error_messages_show_count" : true,
    "error_messages_show_first" : true,

    "extensions" : [".js"],
    "jshintrc" : "/Users/afterdesign/Projects/redsky-linters/JavaScript/jshintrc",

    "show_dot" : true,
    "show_outline" : true,

    "paths" : {
        "osx" : {
            "jshint_path" : "/usr/local/share/npm/bin/jshint",
            "node_path" : "/usr/local/bin/node"
        },
        "windows" : {
            "jshint_path" : "",
            "node_path" : ""
        },
        "linux" : {
            "jshint_path" : "",
            "node_path" : ""
        }
    }
}
```

## Linux & Windows

It should work just fine. You need to set paths for jshint and node.
If you want to add default paths then write issue or create pull request.

# Contact

You can follow me on twitter: [@afterdesign](http://twitter.com/afterdesign)

# License

Licensed under the [MIT license](http://opensource.org/licenses/MIT).