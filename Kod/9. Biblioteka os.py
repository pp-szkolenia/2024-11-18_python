import os

print(os.getcwd())  # get current working directory

print(sorted(os.listdir()))

print(os.listdir("Kod"))

print(os.path.join(os.getcwd(), "Kod"))

print(os.path.isdir("Kod/1. Podstawy.md"))

projects_path = "test_walk_1/projects"
# print([item
#        for item in os.listdir(projects_path)
#        if os.path.isfile(os.path.join(projects_path, item))])


print(os.path.exists("functions.py"))


import os
import shutil

os.mkdir("nowy_folder")
os.rmdir("nowy_folder")

os.makedirs("nowy_folder/podfolder")
shutil.rmtree("nowy_folder")



os.mknod("test.txt")

os.mkdir("folder/subfolder")

shutil.rmtree("folder")
