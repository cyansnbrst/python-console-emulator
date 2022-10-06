#!/usr/bin/python3

import zipfile
import sys
from console import Console

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            with zipfile.ZipFile(sys.argv[1]) as zipfile:  # открытие файла
                directories = zipfile.namelist()  # получение списка всех файлов и папок
                vshell = Console(directories)
                while True:
                    if vshell.current_path == '':
                        print('[~vshell]:/ ', end='')
                    else:
                        print(f'[~vshell]:/{vshell.current_path[:-1]} ', end='')
                    users_input = input()  # ввод пользователем команды + арумента
                    users_input = users_input.split(' ')  # отделяем команду от аргумента

                    # обрабатываем всевозможные команды
                    if users_input[0] == 'pwd':
                        vshell.pwd_command()

                    elif users_input[0] == 'ls':
                        vshell.ls_command(users_input)

                    elif users_input[0] == 'cd':
                        vshell.cd_command(users_input)

                    elif users_input[0] == 'cat':
                        if len(users_input) > 0:
                            file_for_reading = users_input[1]
                            if file_for_reading in vshell.directories:
                                with zipfile.open(f'{vshell.current_path}{file_for_reading}',
                                                  'r') as file:  # открытие файла из архива
                                    for line in file.readlines():
                                        for symbol in line.decode('utf-8').strip():
                                            print(symbol, end='')  # вывод текста из файла
                                        print()
                            else:
                                print(f"cat: can\'t open \'{file_for_reading}\': No such file ")

                    elif users_input[0] == 'exit':
                        break

                    else:
                        print(f'sh: {users_input[0]}: command not found')
        else:
            print('Enter filename')

    except Exception as e:
        print(e)
