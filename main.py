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

while True:
    option = input("Choose what you want to do:\n1. Create a new folder\n2. Print out all folders\n")

    if option == "1" or option == "one":
        folder_name = input("Enter new folder name: ").replace(" ", "_")
        createNewFolder(folder_name)
    elif option == "2" or option == "two":
        printFolders()