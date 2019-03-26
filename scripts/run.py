import os
from time import time
from os import system
from sys import argv

def terminate(s, exitcode = -1):
    print(s)
    exit(exitcode)

if __name__ == '__main__':
    fileName = argv[1]
    dirName = os.path.dirname(fileName)
    baseNameNoExt = os.path.splitext(os.path.basename(fileName))[0]
    start = time()
    print("---Program Started---")
    if fileName.endswith('.cpp'):
        res = system(F'cd {dirName} && {baseNameNoExt}')
        if res:
            terminate(F"Runtime Error with exit code {res}")
        else:
            print(F'\nTime Used:\n{time()-start}')
    elif fileName.endswith(".py"):
        res = os.system(F"cd {dirName} && python {fileName}")
        if res:
            terminate(F"Runtime Error with exit code {res}")
        else:
            print(F"\nTime Used:\n{time()-start}")
    elif fileName.endswith(".java"):
        res = os.system(F'cd {dirName} && java {baseNameNoExt}')
        if res:
            terminate(F"Runtime Error with exit code {res}")
        else:
            print(F"\nTime Used:\n{time()-start}")