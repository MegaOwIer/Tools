# Summary
This is my configuation files of VSCode for Windows.
It has already supported `C++`, `Python` and `Java`.


# Requirs
+ Python 3.6 or later
    + The library `tkinter`


# Setup
First, open your workspace folder and clone this to your computer.
```sh
git clone https://github.com/MegaOwIer/Tools.git ./.vscode

```

Here are some items might need to modify before you use it:
+ Line 17 of `./c_cpp_properties.json` (Full path of the C/C++ compiler being used)
+ Line 18 and 19 of `./c_cpp_properties.json` (Version of the C/C++ language standard to use for IntelliSense)

You can also change other things to make it adapt your personal habits.

# Functions
## Compile & Run (default 'build' task)
You can use it to compile your source code and execute it.

## Run (default 'test' task)
You can use it to execute your code if you have compiled it before.