#!/usr/bin/python3

from zipfile import ZipFile
import sys
from console import Console

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            with ZipFile(sys.argv[1]) as zipfile:
                directories = zipfile.namelist()
                vshell = Console(directories, zipfile)
                while True:
                    if vshell.current_path == '':
                        print("[~vshell]:/ ", end='')
                    else:
                        print(f"[~vshell]:/{vshell.current_path[:-1]} ", end='')
                    users_input = input()
                    users_input = users_input.split(' ')

                    if users_input[0] == "pwd":
                        vshell.pwd_command()

                    elif users_input[0] == "ls":
                        vshell.ls_command(users_input)

                    elif users_input[0] == "cd":
                        vshell.cd_command(users_input)

                    elif users_input[0] == "cat":
                        vshell.cat_command(users_input)
                    else:
                        print(f"vsh: {users_input[0]}: command not found")
        else:
            print("Enter filename")

    except Exception as exception:
        print(exception)
