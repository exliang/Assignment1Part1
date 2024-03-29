
# a1p1.py

# Emily Liang
# exliang@uci.edu
# 79453973

from pathlib import Path


def main():
    user_input()


def user_input():
    while True:
        user_command = input()  # format: [COMMAND] [INPUT] [[-]OPTION] [INPUT]
        command_list = user_command.split()
        command = command_list[0]

        if command == 'Q':
            quit()

        path = command_list[1]
        myPath = Path(path)

        if myPath.exists():  # ensure that directory exists
            if command == 'L':  # list contents of directory
                if len(command_list) == 2:  # [COMMAND] [INPUT]
                    list_directories(myPath)
                elif len(command_list) == 3:  # [COMMAND] [INPUT] [[-]OPTION]
                    option = command_list[2]
                    if option == '-r':
                        recursive(myPath)
                    elif option == '-f':  # output files only
                        list_files(myPath)
                elif len(command_list) == 4:  # [C][I][[-]O][I]
                    option = command_list[2]
                    if option == '-s':  # output files that match the file name
                        file_name = command_list[3]
                        matching_files(myPath, file_name)
                    elif option == '-e':
                        file_extension = command_list[3]
                        matching_extension(myPath, file_extension)
                    elif option == '-r':  # -r -f
                        option2 = command_list[3]
                        recursive_f(myPath)
                elif len(command_list) == 5:  # [C][I][[-]O][I][I]
                    option = command_list[2]
                    option2 = command_list[3]
                    if option == '-r' and option2 == '-s':  # -r -s filename.ex
                        file_name = command_list[4]
                        recursive_s(myPath, file_name)
                    elif option == '-r' and option2 == '-e':  # -r -e fileex
                        file_extension = command_list[4]
                        recursive_e(myPath, file_extension)
        else:
            print("Directory doesn't exist. Try again.")


def list_directories(myPath):
    if any(myPath.iterdir()):  # check if directory isnt empty
        dir_list = []
        file_list = []
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.is_file():  # if is file, put it in the file list
                file_list.append(currentPath)
            elif currentPath.is_dir():  # if it's a dir, put in the dir list
                dir_list.append(currentPath)
        file_list.extend(dir_list)  # combine lists (files first)
        combined_list = file_list
        for directory in combined_list:
            print(directory)


def list_files(myPath):
    if any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.is_file():  # list files only
                print(currentPath)


def matching_files(myPath, file_name):
    if any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.is_file() and currentPath.name == file_name:
                print(currentPath)


def matching_extension(myPath, file_extension):
    if any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.name.endswith(file_extension):  # file type = file e
                print(currentPath)


def recursive(myPath):
    dir_list = []
    if not any(myPath.iterdir()):  # if there's no more folders in directory
        return
    elif any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.is_file():  # if it's a file, print it
                print(currentPath)
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.is_dir():  # if a dir, call func recursively
                dir_list.append(currentPath)
                print(currentPath)
                recursive(currentPath)


def recursive_f(myPath):
    if any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if not currentPath.is_dir():
                print(currentPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_dir():  # if a dir, call func recursively
                recursive_f(currentPath)


def recursive_s(myPath, file_name):
    if any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.is_file() and currentPath.name == file_name:
                print(currentPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_dir():  # if a dir, call func recursively
                recursive_s(currentPath, file_name)


def recursive_e(myPath, file_extension):
    if any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.name.endswith(file_extension):  # file type = file e
                print(currentPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_dir():  # if a dir, call func recursively
                recursive_e(currentPath, file_extension)


if __name__ == '__main__':
    main()

# Citations:
# - https://docs.python.org/3/library/pathlib.html
