import sys
from zipfile import ZipFile


class Console:

    def __init__(self, directories):
        self.current_path = ''
        self.directories = directories

    def pwd_command(self):
        if self.current_path == '':
            print('/')
        else:
            print(f"/{self.current_path[:-1]}")

    def ls_command(self, users_input):
        path = self.current_path
        normal_input = True
        incorrect_input_cases = []
        if len(users_input) != 1:
            path = f'{users_input[1]}/'
            if path[0] == '/':
                path = path[1:]
            if not path in self.directories and path != '/':
                for i in range(1, len(users_input)):
                    if users_input[i] != '':
                        incorrect_input_cases.append(users_input[i])
                if len(incorrect_input_cases) != 0:
                    normal_input = False
        if path == '/':  # if root
            path = ''
        if normal_input:
            folders_and_files = list()
            for folder in self.directories:
                if folder.startswith(path):
                    folder = folder[len(path):]
                    if not (folder.split('/')[0]) in folders_and_files:
                        folders_and_files.append((folder.split('/')[0]))
            for item in folders_and_files:
                if item != '':
                    if item == folders_and_files[-1]:
                        print(item)
                    else:
                        print(item, ' ', end="")
        else:
            for bad in incorrect_input_cases:
                print("ls: " + bad + ": No such file or directory")

    def cd_command(self, users_input):
        input = ''
        for inp in users_input[1:]:
            if inp != '':
                input = inp
                break
        if input == '' or input == '.':
            return
        if input == '..':
            if self.current_path != '':
                path = self.current_path.split('/')
                path = path[:-2]
                path = '/'.join(path)
                if path == '/' or path == '':
                    path = ''
                else:
                    path = path + '/'
                self.current_path = path
        else:
            if input[0] == '/':
                directory = f"{input[1:]}/"
            else:
                directory = f"{self.current_path}{input}/"
            if directory in self.directories:
                self.current_path = directory
            elif directory[:-1] in self.directories:
                print(f"sh: cd: can\'t cd to {input}: Not a directory")
            else:
                print(f"sh: cd: can\'t cd to {input}: No such file or directory")
