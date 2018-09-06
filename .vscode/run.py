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
    baseName = os.path.splitext(fileName)[0]
    start = time()
    if fileName.endswith('.cpp'):
        res = system(F'cd {dirName} && {baseName}')
        if res:
            terminate(F"Runtime Error with exit code {res}")
        else:
            print(F'\nTime Used:\n{time()-start}')
    elif fileName.endswith(".py"):
        if os.system(F"cd {dirName} && python {fileName}"):
            terminate("Runtime error")
        else:
            print(F"\nTime Used:\n{time()-start}")