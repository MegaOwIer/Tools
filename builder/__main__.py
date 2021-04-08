from os.path import basename, dirname, splitext
from argparse import ArgumentParser
from sys import argv

from . import file_extension_map, quit
from .compiler import compile
from .runner import run

if __name__ == '__main__':
    fileName = F'"{argv[1]}"'
    dirName = F'"{dirname(argv[1])}"'
    baseNameNoExt, fileExt = splitext(basename(argv[1]))

    if fileExt not in file_extension_map:
        quit(F'File of type {fileExt} not supported yet.')

    parser = ArgumentParser()
    parser.add_argument('--no-compile', action='store_true')

    if not parser.parse_args(argv[2:]).no_compile:
        compile(fileName, dirName, baseNameNoExt, file_extension_map[fileExt])
    run(fileName, dirName, baseNameNoExt, file_extension_map[fileExt])
