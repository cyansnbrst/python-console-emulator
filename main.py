#!/usr/bin/python3

import zipfile
import sys

if __name__ == '__main__':
    path = ''
    try:
        if len(sys.argv) > 1:
            with zipfile.ZipFile(sys.argv[1]) as zipfile:  # открытие файла
                all_folders = zipfile.namelist()  # получение списка всех файлов и папок
                while True:
                    if path == '':
                        print('[vshell@root ~] ', end='')
                    else:
                        tmp = path.split('/')  # создаем массив из директорий
                        last_path = tmp[-2]  # выбираем предпоследнюю папку
                        print(f'[vshell@root {last_path}] ', end='')
                    split_str = input()  # ввод пользователем команды + арумента
                    split_str = split_str.split(' ')  # отделяем команду от аргумента

                    # обрабатываем всевозможные команды
                    if split_str[0] == 'pwd':
                        print(f'/{path}')  # вывод текущей директории

                    elif split_str[0] == 'ls':
                        correct_args = True
                        incorrect_args = []
                        if len(split_str) != 1:    # проверка на лишние аргументы. если одни пробелы - тогда все ок
                            for i in range(1, len(split_str)):
                                if split_str[i] != '':
                                    incorrect_args.append(split_str[i])
                            if len(incorrect_args) != 0:
                                correct_args = False
                        if correct_args:
                            unic_list = set()  # делаем множество из папок
                            for folder in all_folders:  # перебираем все папки
                                if folder.startswith(path):  # смотрим что у каждой внутри
                                    folder = folder[len(path):]  # обрезаем название папки из пути
                                    unic_list.add(
                                        (folder.split('/')[0]))
                            # выводим всё, кроме пустых строк
                            for el in sorted(unic_list):
                                if el != '':
                                    print(el)
                        else:
                            for x in incorrect_args:
                                print("ls: " + x + ": No such file or directory")

                    elif split_str[0] == 'cd':
                        # Получение новой dir
                        command_str = ' '.join(split_str[1:])
                        if command_str == '..':
                            if path != '':  # проверка на некорневую dir
                                tmp = path.split('/')
                                tmp = tmp[:-2]  # обрезаем последние два элемента списка
                                # (dir, в которой мы находимся и пустой элемент)
                                tmp = '/'.join(tmp)
                                if tmp == '/' or tmp == '':  # если находимся в корневой dir
                                    tmp = ''
                                else:
                                    tmp = tmp + '/'
                                path = tmp  # преобразование временной dir в текущую
                        else:
                            tmp_dir = f'{path}{command_str}/'
                            if tmp_dir in all_folders:  # если данная dir существует в листе всех папок
                                path = tmp_dir  # преобразование временной dir в текущую
                            else:
                                print(f'sh: cd: {command_str}: No such file or directory')
                    elif split_str[0] == 'cat':
                        f = ' '.join(split_str[1:])  # соединение аргумента через пробелы
                        with zipfile.open(f'{path}{f}', 'r') as file:  # открытие файла из архива
                            for a in file.readlines():
                                for b in a.decode('utf-8').strip():
                                    print(b, end='')  # вывод текста из файла
                                print()
                    elif split_str[0] == 'exit':
                        break
                    else:
                        print(f'sh: {split_str[0]}: command not found')
        else:
            print('Enter filename')
    except Exception as e:
        print(e)
