import os
from CONSTS import *

def checkPath():
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)

def createNewFolder(folder_name):
    checkPath()
    os.chdir(FOLDER_PATH)
    try:
        os.mkdir(folder_name)
        print(f"Folder {folder_name} creates successfully!")
    except FileExistsError:
        print(f"Folder {folder_name} already exists.")
    except PermissionError:
        print(f"No permission to create a new folder.")
    os.chdir("..")

def printFolders():
    checkPath()
    folders = os.walk(FOLDER_PATH)
    for folder in folders:
        print(folder[0])
    print("")

def renameFolder(old_folder, new_folder):
    checkPath()
    folders = os.walk(FOLDER_PATH)
    for folder in folders:
        if f"Folders/{old_folder}" == folder[0]:
            os.rename(f"Folders/{old_folder}", f"Folders/{new_folder}")
            return 0
    print("Folder with provided name doesn't exist.\n")

while True:
    option = input("Choose what you want to do:\n1. Create a new folder\n2. Print out all folders\n3. Edit folder name\n").lower()

    if option == "1" or option == "one":
        folder_name = input("Enter new folder name: ").replace(" ", "_")
        createNewFolder(folder_name)
    elif option == "2" or option == "two":
        printFolders()
    elif option == "3" or option == "three":
        old_folder = input("Enter folder name you want to rename (empty space will be replaced with underscore '_' sign): ").replace(" ", "_")
        new_folder = input("Enter new name of a folder: ").replace(" ", "_")
        if old_folder == new_folder:
            print("Names must be different.")
        else:
            renameFolder(old_folder, new_folder)
    else:
        print("Please input correct number.")