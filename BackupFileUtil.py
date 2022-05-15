#!python3
# BackupFileUtil.py -- Manage files and directories to store on a backup drive
# INCOMPLETE 

from pathlib import Path
import os, shelve

WELCOME_MESSAGE = " BackupFileUtil "
WELCOME_PARA = """
\nUse this script to store and manage files and directories that you
wish to save to an external drive. If this is a first time setup,
please select 1.
\n"""
USER_OPTIONS = {
        1: "First time setup",
        2: "Add new file path",
        3: "View existing file paths",
        4: "Run Backup",
        5: "README",
    }

# Add main program directory
def add_main_dir() -> None:
    main_dir = Path(Path.home()) / "BackupFileUtil"
    if main_dir.exists() == False:
        os.makedirs(main_dir)
        
# Add new file paths
def edit_text_file(new_name, new_path) -> None:
    stored_paths = open(Path.home() / "BackupFileUtil\\storedPaths.txt", "a")
    stored_paths.write(new_name + '\n')
    stored_paths.write(new_path + '\n')
    stored_paths.close()

# View all available storage / optical drives        
def return_drives() -> list:
    DRIVE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return list(letter + ':\\' for letter in DRIVE_LETTERS if Path(letter + ':\\').exists())

# Return existing file paths
def get_paths() -> list:
    stored_paths = open(Path.home() / "BackupFileUtil\\storedPaths.txt", "r")
    path_list = stored_paths.readlines()
    stored_paths.close()
    return path_list

def overwrite_dir(source: str, destination: str) -> None:
     shutil.copytree(source, destination, dirs_exist_ok=True)

def overwrite_files(source: str, destination: str) -> None:
     shutil.copy(source, destination)
     
# copy files and directories
def back_up_files(sources: list, destination: str) -> None:
    for file_path in sources:
        file_path = file_path.strip('\n')
        path_object = Path(file_path)
        if path_object.is_dir() == True:      
            overwrite_dir(path_object, destination + path_object.name)
        elif path_object.is_file() == True and Path(destination + (path_object.parent.name)).exists() == False:
            os.mkdir(destination + path_object.parent.name)
            overwrite_files(path_object, destination + path_object.parent.name + '\\' + path_object.name)
        elif path_object.is_file():            
            overwrite_files(path_object, destination + path_object.parent.name + '\\' + path_object.name)

def main():
    # print startup messages
    print('\n', WELCOME_MESSAGE.center(68, "-"), WELCOME_PARA)
    for number, message in USER_OPTIONS.items():
        print(message.ljust(30, ".") + str(number).rjust(2))

    # main selection loop
    while True:    
        choice = str(input())
        if choice not in '12345':
            print('Invalid selection\n')
            continue
        elif main(choice):
            pass
        elif not main(choice):
            break
    # TODO: Execute commands from user input
    if user_input == '1':
        pass
        
    # Optionally print existing file paths
    if user_input == '3':
        x = source_config.return_paths()
        print(x)
        return True

    # TODO: optionally write to .txt file based on user input

    # TODO: optionally backup files


if __name__ == "__main__":
    main()


            
