from zipfile import ZipFile
__all__ = ZipFile

class Console:

    def __init__(self, directories, zipfile):
        self.current_path = ''
        self.directories = directories
        self.zipfile = zipfile

    def start(self):
        if self.current_path == '':
            print("[~vshell]:/ ", end='')
        else:
            print(f"[~vshell]:/{self.current_path[:-1]} ", end='')
        users_input = input()
        self.users_input = users_input.split(' ')

        if self.users_input[0] == "pwd":
            self.pwd_command()

        elif self.users_input[0] == "ls":
            self.ls_command()

        elif self.users_input[0] == "cd":
            self.cd_command()

        elif self.users_input[0] == "cat":
            self.cat_command()
        else:
            print(f"sh: {self.users_input[0]}: command not found")

    def pwd_command(self):
        if self.current_path == '':
            print('/')
        else:
            print(f"/{self.current_path[:-1]}")

    def ls_command(self):
        path = self.current_path
        normal_input = True
        incorrect_input_cases = []
        if len(self.users_input) != 1:
            path = f'{self.users_input[1]}/'
            if path[0] == '/':
                path = path[1:]
            if not path in self.directories and path != '/':
                for i in range(1, len(self.users_input)):
                    if self.users_input[i] != '':
                        incorrect_input_cases.append(self.users_input[i])
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

    def cd_command(self):
        input = ''
        for inp in self.users_input[1:]:
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
                    path += '/'
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

    def cat_command(self):
        all_files = []
        for file in self.users_input[1:]:
            if file != '':
                all_files.append(file)
        if len(all_files) > 0:
            for file_for_reading in all_files:
                if file_for_reading[0] == '/':
                    file_for_reading = file_for_reading[1:]
                if f"{self.current_path}{file_for_reading}" in self.directories:
                    with self.zipfile.open(f"{self.current_path}{file_for_reading}", 'r') as file:
                        for line in file.readlines():
                            for symbol in line.decode('utf-8').strip():
                                print(symbol, end="")
                            print()
                else:
                    print(f"cat: can\'t open \'{file_for_reading}\': No such file ")
        else:
            return
