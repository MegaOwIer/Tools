from time import time
from os import system
from os.path import basename, dirname, splitext
from sys import argv

from . import file_extension_map, quit

def run(fileName, dirName, baseNameNoExt, language):
    start = time()
    print("---Program Started---")
    if language == 'c' or language == 'c++':
        res = system(F'cd {dirName} && {baseNameNoExt}')
        if res:
            quit(F"Runtime Error with exit code {res}")
        else:
            print(F'\nTime Used:\n{time() - start}')
    elif language == 'python':
        res = system(F'cd {dirName} && python {fileName}')
        if res:
            quit(F"Runtime Error with exit code {res}")
        else:
            print(F"\nTime Used:\n{time() - start}")
    elif fileName.endswith(".java"):
        res = system(F'cd {dirName} && java {baseNameNoExt}')
        if res:
            quit(F"Runtime Error with exit code {res}")
        else:
            print(F"\nTime Used:\n{time()-start}")

if __name__ == '__main__':
    fileName = F'"{argv[-1]}"'
    dirName = F'"{dirname(argv[-1])}"'
    baseNameNoExt, fileExt = splitext(basename(argv[-1]))

    if fileExt not in file_extension_map:
        quit(F'File of type {fileExt} not supported yet.')

    run(fileName, dirName, baseNameNoExt, file_extension_map[fileExt])
