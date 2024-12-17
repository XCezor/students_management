import os
from CONSTS import *

def createNewFolder(folder_name):
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
    os.chdir(FOLDER_PATH)
    try:
        os.mkdir(folder_name)
        print(f"Folder {folder_name} creates successfully!")
    except FileExistsError:
        print(f"Folder {folder_name} already exists.")
    except PermissionError:
        print(f"No permission to create a new folder.")
    os.chdir("..")

while True:
    option = input("Choose what you want to do:\n1. Create a new folder\n")

    if option == "1" or option == "one":
        folder_name = input("Enter new folder name: ").replace(" ", "_")
        createNewFolder(folder_name)