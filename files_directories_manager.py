import os
import shutil


def create_file(name):
    with open(name, "w"):
        pass


def create_folder(name):
    os.mkdir(name)


def delete_file(name):
    os.remove(name)


def delete_folder(name):
    shutil.rmtree(name)


def move(src, dest):
    shutil.move(src, dest)


def copy(src, dest):
    if os.path.isdir(src):
        shutil.copytree(src, dest)
    else:
        shutil.copy(src, dest)


""" Пример использования """
# create_file("example.txt")
# create_folder("new_folder")
# copy("example.txt", "new_folder/example_copy.txt")
# move("new_folder/example_copy.txt", "new_folder/copied_files/example_copy.txt")
# delete_file("example.txt")
# delete_folder("new_folder")
