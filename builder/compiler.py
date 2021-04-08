from os import system
from tkinter import Button, Entry, StringVar, Tk, ttk

from . import quit

class c_cpp_Compile:
    def __init__(self, fileName, dirName, baseNameNoExt, language):
        self.fileName = fileName
        self.dirName = dirName
        self.baseNameNoExt = baseNameNoExt
        self.language = language

        self.popup_initialization()

    def popup_initialization(self):
        self.compileOptions = Tk()
        self.compileOptions.geometry('256x144')
        self.compileOptions.title('C/C++ Compile Options')

        # Standard
        lb = ttk.Label(self.compileOptions, text='Standard:  ')
        lb.grid(column=0, row=0)
        lb.columnconfigure(0, weight=1)
        self.standard = StringVar()
        stdChosen = ttk.Combobox(self.compileOptions, textvariable=self.standard, state='readonly')
        if self.language == 'c++':
            stdChosen['values'] = ('c++03', 'c++11', 'c++14', 'c++17', 'c++2a')
        else:
            stdChosen['values'] = ('c89', 'c99', 'c11')
        stdChosen.grid(column=1, row=0)
        stdChosen.columnconfigure(1, weight=3)
        stdChosen.current(2 if self.language == 'c++' else 1)

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
        self.extra.set('-Wall -Wextra -Wconversion -Wshadow -Wl,--stack=1048576000')
        extraset = Entry(self.compileOptions, textvariable=self.extra, width=40)
        extraset.grid(column=0, row=3, columnspan=2, sticky='w')

        Button(self.compileOptions, text='Go!', command=self.on_click).grid(column=0, row=5, columnspan=2)
        self.compileOptions.bind(sequence="<Return>", func=self.on_click)
        self.compileOptions.bind(sequence="<Escape>", func=quit)

        self.compileOptions.mainloop()
    
    def on_click(self, argv = list()):
        command = F'g++ {self.fileName} -o {self.baseNameNoExt} -std={self.standard.get()} {self.optimize.get()} {self.extra.get()}\n'
        print(command)
        self.compileOptions.destroy()
        self.compile_res = system(F'cd {self.dirName} && {command}')


class javaCompile:
    def __init__(self, fileName, dirName, baseNameNoExt):
        command = F'javac {baseNameNoExt}.java\n'
        print(command)
        self.compileres = system(F'cd {dirName} && {command}')


def compile(fileName, dirName, baseNameNoExt, language):
    if language == 'c' or language == 'c++':
        if c_cpp_Compile(fileName, dirName, baseNameNoExt, language).compile_res:
            quit("Compile Error")
        else:
            print("---Compile Success---")
    elif language == 'python':
        pass
    elif language == 'java':
        if javaCompile(fileName, dirName, baseNameNoExt).compileres:
            quit("Compile Error")
        else:
            print("---Compile Success---")
