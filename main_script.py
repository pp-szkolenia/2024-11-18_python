import os
from pprint import pprint


for root, dirs, files in os.walk("test_walk"):
    for file in files:
        if file.split(".")[-1] == "txt":
            with open(os.path.join(root, file), "r") as f:
                print(f.read(), "\n")


