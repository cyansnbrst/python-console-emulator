#!/usr/bin/python3

from zipfile import ZipFile
import sys
from console import Console

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            with ZipFile(sys.argv[1]) as zipfile:
                directories = zipfile.namelist()
                vshell = Console(directories)
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
                        all_files = []
                        for file in users_input[1:]:
                            if file != '':
                                all_files.append(file)
                        if len(all_files) > 0:
                            for file_for_reading in all_files:
                                if file_for_reading[0] == '/':
                                    file_for_reading = file_for_reading[1:]
                                if file_for_reading in vshell.directories:
                                    with zipfile.open(f"{vshell.current_path}{file_for_reading}", 'r') as file:
                                        for line in file.readlines():
                                            for symbol in line.decode('utf-8').strip():
                                                print(symbol, end="")
                                            print()
                                else:
                                    print(f"cat: can\'t open \'{file_for_reading}\': No such file ")
                        else:
                            continue
                    else:
                        print(f"vsh: {users_input[0]}: command not found")
        else:
            print("Enter filename")

    except Exception as exception:
        print(exception)
