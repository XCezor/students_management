# Students Management Instruction
## Functionality
User is asked to choose an option. Each option triggers different functions. The program is meant to create new folders to later manage students.

## Basic Functions
- checkPath(): Is triggered always when manipulating folders. Checks if the path Folders/ exists and if not, it will create a new one.

- createNewFolder(folder_name): User is asked to provide a new folder name. If the name is not already occupied, the new folder inside Folders/ path is created.

- printFolders(): Prints out all existing folders in the Folders/ directory.

- renameFolder(old_folder, new_folder): User is asked to provide a name of a folder that needs to be renamed and a new name to replace it. If the names are equal or if the new name already exists, it returns an error with info.

- removeFolder(folder_name): Asks user for a name to remove. If folder exists in the Folders/ directory, it will be removed.