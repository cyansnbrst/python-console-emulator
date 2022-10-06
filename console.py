import zipfile

class Console:

    def __init__(self, directories):
        self.current_path = ''
        self.directories = directories

    def pwd_command(self):
        if self.current_path == '':
            print('/')
        else:
            print(f'/{self.current_path[:-1]}')  # вывод текущей директории

    def ls_command(self, users_input):
        path = self.current_path
        normal_input = True
        incorrect_input_cases = []
        if len(users_input) != 1:
            path = f'{users_input[1]}/'
            if path[0] == '/':  # если абсолютный путь
                path = path[1:]
                print(path)
            if not path in self.directories and path != '/':
                for i in range(1,
                               len(users_input)):  # проверка на лишние аргументы. если одни пробелы - тогда все ок
                    if users_input[i] != '':
                        incorrect_input_cases.append(users_input[i])
                if len(incorrect_input_cases) != 0:
                    normal_input = False
        if path == '/':  # снова проверяем корень, тк слеш у него не уберется
            path = ''
        if normal_input:
            folders_and_files = set()  # делаем множество из папок
            for folder in self.directories:  # перебираем все папки
                if folder.startswith(path):  # смотрим что у каждой внутри
                    folder = folder[len(path):]  # обрезаем название папки из пути
                    folders_and_files.add(
                        (folder.split('/')[0]))
            # выводим всё, кроме пустых строк
            for item in sorted(folders_and_files):
                if item != '':
                    print(item, ' ', end="")
        else:
            for bad in incorrect_input_cases:
                print("ls: " + bad + ": No such file or directory")

    def cd_command(self, users_input):
        # получение новой директории
        input = ' '.join(users_input[1:])
        if input == '..':  # родительская директория
            if self.current_path != '':  # проверка на некорневую dir
                path = self.current_path.split('/')
                path = path[:-2]  # обрезаем последние два элемента списка
                # (dir, в которой мы находимся и пустой элемент)
                path = '/'.join(path)
                if path == '/' or path == '':  # если находимся в корневой dir
                    path = ''
                else:
                    path = path + '/'
                self.current_path = path
        elif input == '.':  # та же директория
            return
        else:
            if input[0] == '/':  # если абсолютный путь
                directory = f'{input[1:]}/'
            else:
                directory = f'{self.current_path}{input}/'  # если обычный
            if directory in self.directories:  # если данная dir существует в листе всех папок
                self.current_path = directory  # преобразование временной dir в текущую
            elif directory[:-1] in self.directories:
                print(f'sh: cd: can\'t cd to {input}: Not a directory')  # если файл
            else:
                print(f'sh: cd: can\'t cd to {input}: No such file or directory')