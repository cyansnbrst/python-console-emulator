#!/usr/bin/python3

from zipfile import ZipFile
import sys
from console import Console

if __name__ == '__main__':
    try:
        with ZipFile(sys.argv[1]) as zipfile:
            directories = zipfile.namelist()
            vshell = Console(directories, zipfile)
            while True:
                vshell.start()

    except Exception as exception:
        print(exception)
