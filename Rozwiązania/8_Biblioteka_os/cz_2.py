import os
import shutil


os.mkdir("nowy_folder")
os.rmdir("nowy_folder")

os.makedirs("nowy_folder/podfolder")
shutil.rmtree("nowy_folder")


for root, dirs, files in os.walk("test_walk"):
    for file in files:
        if file.split(".")[-1] == "txt":
            with open(os.path.join(root, file), "r") as f:
                print(f.read(), "\n")