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
6. use ```ctrl+super+j``` to run

## Default settings:

```
{
    "run" : {
        "on_load" : true,
        "on_save" : true
    },
    "extensions" : [".js"],
    "jshintrc" : "",
    "show" : {
        "dot" : true,
        "outline" : true
    },
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