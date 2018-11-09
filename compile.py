import os
from sys import *
from time import time
from tkinter import *
from tkinter import ttk

def cppCompile():
    compileOptions = Tk()
    compileOptions.geometry('300x200')
    compileOptions.title('C++ Compile Options')

    # Standard
    lb = ttk.Label(compileOptions, text = 'Standard:  ')
    lb.grid(column = 0, row = 0)
    lb.columnconfigure(0, weight = 1)
    standard = StringVar()
    stdChosen = ttk.Combobox(compileOptions, textvariable = standard, state = 'readonly')
    stdChosen['values'] = ('c++98', 'c++11', 'c++14', 'c++17', 'c++2a')
    stdChosen.grid(column = 1, row = 0)
    stdChosen.columnconfigure(1, weight = 3)
    stdChosen.current(2)

    # Optimize
    lb = ttk.Label(compileOptions, text = 'Optimize:  ')
    lb.grid(column = 0, row = 1)
    lb.columnconfigure(0, weight = 1)
    optimize = StringVar()
    optChosen = ttk.Combobox(compileOptions, textvariable = optimize, state = 'readonly')
    optChosen['values'] = ('-O0', '-O1', '-O2', '-O3', '-Ofast')
    optChosen.grid(column = 1, row = 1)
    optChosen.columnconfigure(1, weight = 3)
    optChosen.current(2)

    # Extra Options
    lb = ttk.Label(compileOptions, text = 'Extra Compile Options:')
    lb.grid(column = 0, row = 2, columnspan = 2, sticky = 'w')
    extra = StringVar()
    extra.set('-Wall -Wextra')
    extraset = Entry(compileOptions, textvariable = extra, width = 40)
    extraset.grid(column = 0, row = 3, columnspan = 2, sticky = 'w')

    # With grader
    lb = ttk.Label(compileOptions, text = 'With grader:  ')
    lb.grid(column = 0, row = 4)
    lb.columnconfigure(0, weight = 1)
    grader = StringVar()
    graderChosen = ttk.Combobox(compileOptions, textvariable = grader, state = 'readonly')
    graderChosen['values'] = ('Yes', 'No')
    graderChosen.grid(column = 1, row = 4)
    graderChosen.columnconfigure(1, weight = 3)
    graderChosen.current(1)

    def on_click():
        global compileres
        if grader.get() == 'No':
            command = F'g++ {fileName} -o {baseName} -std={standard.get()} {optimize.get()} {extra.get()}\n'
        else:
            command = F'g++ {fileName} {dirName}/grader.cpp -o {baseName} -std={standard.get()} {optimize.get()} {extra.get()}\n'
        compileOptions.destroy()
        print('> ' + command)
        compileres = os.system(command)

    Button(compileOptions, text = 'Go!', command = on_click).grid(column = 0, row = 5, columnspan = 2)

    compileOptions.mainloop()
    return compileres

def terminate(s, exitcode = -1):
    print(s)
    exit(exitcode)

if __name__ == "__main__":
    global fileName, dirName, baseName
    fileName = argv[1]
    dirName = os.path.dirname(fileName)
    baseName = os.path.splitext(fileName)[0]
    if fileName.endswith(".cpp"):
        if cppCompile():
            terminate("Compile Error")
        else:
            print("---Compile Success---")
    elif fileName.endswith(".py"):
        pass
