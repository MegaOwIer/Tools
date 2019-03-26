# Summary
This is my configuation files of VSCode for Windows.
It has already supported `C++`, `Python` and `Java`(incomplete).


# Requirs
+ Python 3.6 or later. You need to install the following packages via pip:
    + The package `tkinter`
+ The following extensions for VSCode are recommended:
    + `C/C++`(ms-vscode.cpptools)
    + `C++ Intellisense`(austin.code-gnu-global)
    + `Python`(ms-python.python)


# Setup
To begin with, open your workspace folder and clone this to your computer.
```sh
git clone https://github.com/MegaOwIer/Tools.git ./.vscode

```

Here are some items need to  be modified before using it:
+ Line 17 of `./c_cpp_properties.json` (Full path of the C/C++ compiler)
+ Line 18 and 19 of `./c_cpp_properties.json` (Version of the C/C++ language standard to use for intellisense)

You can also change other things to make it adapt to your personal habits.

# Functions
## Compile & Run (default 'build' task)
You can use it to compile your source code and execute it.

## Run (default 'test' task)
You can use it to execute your code if you have compiled it before.