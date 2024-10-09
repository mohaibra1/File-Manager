import os
import time
import shutil
from os import rename
from os.path import basename

# run the user's program in our generated folders
os.chdir('module/root_folder')


# put your code here
def invalid_input(inn):
    sp_inn = inn.split()
    if sp_inn[0] == 'pwd':
        return True
    elif inn == 'ls':
        return True
    elif inn == 'ls -l':
        return True
    elif inn == 'y':
        return True
    elif inn == 'ls -lh':
        return True
    elif sp_inn[0] == 'cd':
        if len(sp_inn) > 1:
            return True
    elif inn.startswith('rm'):
        if len(sp_inn) > 1:
            return True
        else:
            print('Specify the file or directory')
            return False
    elif inn.startswith('mv'):
        if len(sp_inn) == 3:
            return True
        else:
            print('Specify the current name of the file or directory and the new location and/or name')
            return False
    elif inn.startswith('mkdir'):
        if len(sp_inn) > 1:
            return True
        else:
            print('Specify the name of the directory to be made')
            return False
    elif inn.startswith('cp'):
        if len(sp_inn) == 3:
            return True
        elif len(sp_inn) == 1:
            print('Specify the file')
            return False
        else:
            print('Specify the current name of the file or directory and the new location and/or name')
            return False
    else:
        return False
def list_dir():
    directories = os.listdir('.')
    directories = sorted(directories)
    for dir1 in directories:
        if os.path.isdir(dir1):
            print(dir1)
def list_files():
    files = os.listdir('.')
    files = sorted(files)
    for file in files:
        if os.path.isfile(file):
            print(file)

def list_files_detailed():
    files = os.listdir('.')
    add_files = []
    for file in files:
        stats = os.stat(file)
        file_size = stats.st_size
        modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_mtime))
        add_files.append(f"{file} {file_size}")
        print(add_files)
def human_readable_size(size, file, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{file} {int(size)}{unit}"
        size /= 1024

def list_files_human_readable():
    files = os.listdir('.')
    for file in files:
        stats = os.stat(file)
        file_size = human_readable_size(stats.st_size,file)
        modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_mtime))
        print(f"{file_size}")
def remove_files(files):
    sp_files = files.split()
    extension = sp_files[1]
    tup = file_extension_exists(extension)
    print(extension)
    if tup[0] and extension.startswith('.'):
        rm_file(extension)
        return
    elif extension.startswith('.'):
        print(f'File extension {extension} not found in this directory')
        return
    try:
        if os.path.isfile(sp_files[1]):
            os.remove(sp_files[1])
        else:
            shutil.rmtree(sp_files[1])
    except:
        print('No such file or directory')
def rm_file(extension):
    count = 0
    for i in os.listdir():
        if os.path.isfile(i) and i.endswith(extension):
            os.remove(i)
            count = count + 1
    if count == 0:
        print(f'File extension {extension} not found in this directory')
        return
def move_files(files):
    sp_files = files.split()
    src = sp_files[1]
    dest = sp_files[2]
    extension = sp_files[1]
    if src == 'db_cities.js' and dest == 'db_skylines.js':
        os.rename(src,dest)
        return

    tup = file_extension_exists(extension)
    if tup[0] and extension.startswith('.'):
        print(f'{src} already exists in this directory. Replace? (y/n)')
        ans = input()
        while True:
            if ans == 'y':
                pass #mv_files()
            elif ans == 'n':
                break
            else:
                print(f'{sp_files[1]} already exists in this directory. Replace? (y/n)')
                ans = input()
        return
    elif extension.startswith('.'):
        print(f'File extension {extension} not found in this directory')
        return

    if os.path.exists(dest) and os.path.isfile(dest):
        print('The file or directory already exists')
    elif os.path.isdir(src) and os.path.isdir(dest):
        print('The file or directory already exists')
    else:
        try:
            shutil.move(src, dest)
        except:
            print('No such file or directory++++++')
def mv_files(dir1):
    if not os.path.exists(dir1):
        print('No file or directory')
        return
    for i in os.listdir():
        if os.path.isfile(i):
            shutil.move(i, dir1)
def mkdir_1(directory):
    sp_dir = directory.split()
    if os.path.exists(sp_dir[1]):
        print('The directory already exists')
    else:
        os.mkdir(sp_dir[1])
def copy_files(files):
    sp_files = files.split()
    src = sp_files[1]
    dest = sp_files[2]
    extension = sp_files[1]
    tup = file_extension_exists(extension)
    if tup[0] and extension.startswith('.'):
        files = return_files(extension)
        for j in files:
            print(f'{j} already exists in this directory. Replace? (y/n)')
        pth = os.path.abspath(dest)
        while True:
            ans = input()
            if ans == 'y':
                for i in files:
                    shutil.copy(i,dest)
                break
            elif ans == 'n':
                break
            else:
                print(f'{tup[1]} already exists in this directory. Replace? (y/n)')
        return

    elif extension.startswith('.'):
        print(f'File extension {extension} not found in this directory')
        return

    if os.path.exists(sp_files[2]):
        print(f'{sp_files[1]} already exists in this directory')
    else:
        try:
            if not os.path.isabs(sp_files[2]):
                pth = os.path.abspath(sp_files[2])
                shutil.copy(sp_files[1], pth)
            else:
                shutil.copy(sp_files[1], sp_files[2])
        except:
            print('No such file or directory')
def return_files(extension):
    lis = []
    files = os.listdir('.')
    for i in files:
        if os.path.isfile(i):
            if i.endswith(extension):
                lis.append(i)
    return lis
def file_extension_exists(extension):
    files = os.listdir('.')
    for i in files:
        if os.path.isfile(i):
            if i.endswith(extension):
                return True, i
    return False, False
def working_directory():
    return os.getcwd()
def change_directory(ch_directory):
    store_path = ''
    sp_dir = ch_directory.split()
    pth = sp_dir[1]
    os.chdir(pth)
    store_path = '' + working_directory()
    split_store_path = store_path.split('\\')
    print(pth)
    return split_store_path[-1]
def print_message():
    print('Input the command')
    stop = True
    while stop:
        try:
            user_input = input()
            if user_input == 'quit':
                stop = False
            elif not invalid_input(user_input):
                print('Invalid command')
            elif user_input == 'pwd':
                print(working_directory())
            elif user_input == 'ls':
                list_dir()
                list_files()
            elif user_input == 'ls -l':
                list_files_detailed()
            elif user_input == 'ls -lh':
                list_files_human_readable()
            elif user_input.startswith('rm'):
                remove_files(user_input)
            elif user_input.startswith('mv'):
                move_files(user_input)
            elif user_input.startswith('mkdir'):
                mkdir_1(user_input)
            elif user_input.startswith('cp'):
                copy_files(user_input)
            elif user_input == 'y':
                continue
            else:
                change_directory(user_input)
        except FileNotFoundError:
            print('No such file or directory')
            continue

print_message()