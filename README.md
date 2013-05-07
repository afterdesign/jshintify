# yet another jshint plugin for sublime

## How to install (mac os version) ?

1. ```brew install nodejs``` - this will take while
2. add ```/usr/local/share/npm/bin``` to $PATH
3. ```npm install jshint```
4. install jshintify sublime package (for now only git):

    ```
    cd $PATH_OF_SUBLIME_PACKAGES
    git clone git://github.com/afterdesign/jshintify.git
    ```
5. open preferences and check if the paths for node and jshint are correct
6. set the path to your jshint file
7. use ```ctrl+super+j``` to run
8. use ``` ctrl+shift+j``` to show list of errors in current line

## Default settings:

1. ```run_on_load``` - run jshint right after file is loaded do editor
2. ```run_on_save``` - run jshint after file is saved
3. ```error_messages_show_count``` and ```error_messages_show_first```
	without ```error_messages_show_count``` show message like:

	```
	(error) : Expected 'for' to have an indentation at 13 instead at 9.
	```
	
	with ```error_messages_show_count``` show message like:
	
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