import os
from sys import argv
from time import time
from tkinter import Button, Entry, StringVar, Tk, ttk


class cppCompile:
    def __init__(self):
        self.compileOptions = Tk()
        self.compileOptions.geometry('300x200')
        self.compileOptions.title('C++ Compile Options')

        # Standard
        lb = ttk.Label(self.compileOptions, text='Standard:  ')
        lb.grid(column=0, row=0)
        lb.columnconfigure(0, weight=1)
        self.standard = StringVar()
        stdChosen = ttk.Combobox(self.compileOptions, textvariable=self.standard, state='readonly')
        stdChosen['values'] = ('c++03', 'c++11', 'c++14', 'c++17', 'c++2a')
        stdChosen.grid(column=1, row=0)
        stdChosen.columnconfigure(1, weight=3)
        stdChosen.current(2)

        # Optimize
        lb = ttk.Label(self.compileOptions, text='Optimize:  ')
        lb.grid(column=0, row=1)
        lb.columnconfigure(0, weight=1)
        self.optimize = StringVar()
        optChosen = ttk.Combobox(self.compileOptions, textvariable=self.optimize, state='readonly')
        optChosen['values'] = ('-O0', '-O1', '-O2', '-O3', '-Ofast')
        optChosen.grid(column=1, row=1)
        optChosen.columnconfigure(1, weight=3)
        optChosen.current(2)

        # Extra Options
        lb = ttk.Label(self.compileOptions, text='Extra Compile Options:')
        lb.grid(column=0, row=2, columnspan=2, sticky='w')
        self.extra = StringVar()
        self.extra.set('-Wall -Wextra -fno-stack-limit')
        extraset = Entry(self.compileOptions, textvariable=self.extra, width=40)
        extraset.grid(column=0, row=3, columnspan=2, sticky='w')

        # With grader
        lb = ttk.Label(self.compileOptions, text = 'With grader:  ')
        lb.grid(column=0, row=4)
        lb.columnconfigure(0, weight=1)
        self.grader = StringVar()
        graderChosen = ttk.Combobox(self.compileOptions, textvariable=self.grader, state='readonly')
        graderChosen['values'] = ('Yes', 'No')
        graderChosen.grid(column=1, row=4)
        graderChosen.columnconfigure(1, weight=3)
        graderChosen.current(1)

        Button(self.compileOptions, text='Go!', command=self.on_click).grid(column=0, row=5, columnspan=2)
        self.compileOptions.bind(sequence="<Return>", func=self.on_click)
        self.compileOptions.bind(sequence="<Escape>", func=terminate)

        self.compileOptions.mainloop()
    
    def on_click(self, argv = list()):
        if self.grader.get() == 'No':
            command = F'g++ {fileName} -o {baseNameNoExt} -std={self.standard.get()} {self.optimize.get()} {self.extra.get()}\n'
        else:
            command = F'g++ {fileName} grader.cpp -o {baseNameNoExt} -std={self.standard.get()} {self.optimize.get()} {self.extra.get()}\n'
        print(command)
        self.compileOptions.destroy()
        self.compileres = os.system(F'cd {dirName} && {command}')


class javaCompile:
    def __init__(self):
        command = F'javac {baseNameNoExt}.java\n'
        print(command)
        self.compileres = os.system(F'cd {dirName} && {command}')


def terminate(s, exitcode = -1):
    print(s)
    exit(exitcode)


if __name__ == "__main__":
    global fileName, dirName, baseNameNoExt
    fileName = argv[1]
    dirName = os.path.dirname(fileName)
    baseNameNoExt = os.path.splitext(os.path.basename(fileName))[0]
    if fileName.endswith(".cpp"):
        if cppCompile().compileres:
            terminate("Compile Error")
        else:
            print("---Compile Success---")
    elif fileName.endswith(".py"):
        pass
    elif fileName.endswith(".java"):
        if javaCompile().compileres:
            terminate("Compile Error")
        else:
            print("---Compile Success---")
