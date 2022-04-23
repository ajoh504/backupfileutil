#!python3
# BackupFileUtil.py -- Manage files and directories to store on a backup drive

from pathlib import Path
import os, shelve

# Configure files on source drive
class source_config:
    def __init__(self):
        pass
    # Retrieve user's home directory, check if BackupFileUtil dir exists
    def add_main_dir() -> None:
        new_dir = Path(Path.home()) / "BackupFileUtil"
        if new_dir.exists() == False:
            os.makedirs(new_dir)
        
    # Create / edit .txt file for storing file paths
    def manage_text_file(new_name, new_path) -> None:
        os.chdir(Path(Path.home()) / "BackupFileUtil")
        stored_paths = open("storedPaths.txt", "w")
        stored_paths.write(new_name, new_path)
        stored_paths.close()

    # return stored file paths
    def return_paths() -> str:
        os.chdir(Path(Path.home()) / "BackupFileUtil")
        stored_paths = open("storedPaths.txt", "w")

# TODO: Configure files on backup drive
class backup_config:
    def __init__(self):
        pass
    # Return all existing drives
    def return_drives() -> list:
        DRIVE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return list(letter + ':\\' for letter in DRIVE_LETTERS if Path(letter + ':\\').exists():

    # TODO: if copying file, create parent directory in backup location
    def create_parent():
        

    # TODO: if copying directory, create it in backup location
        
# TODO: copy files and directories
def backup_task():
    pass
        
def main(user_input: int) -> int: 
    # TODO: Execute commands from user input
    if user_input == 1:
        pass
        
    # TODO: optionally print existing file paths

    # TODO: optionally write to .txt file based on user input

    # TODO: optionally backup files


if __name__ == "__main__":
    WELCOME_MESSAGE = " Welcome to BackupFileUtil v. 1.0 "
    WELCOME_PARA = """
\nUse this script to store and manage files and directories that you
wish to save to an external drive. If this is a first time setup,
please select 1.

Otherwise, select 2 to add new file paths, 3 to view existing file
paths, 4 to run the backup, or 5 to view the README.\n"""
    USER_OPTIONS = {
        1: "First time setup",
        2: "Add new file path",
        3: "View existing file paths",
        4: "Run Backup",
        5: "README",
    }
    # print startup messages
    print('\n', WELCOME_MESSAGE.center(68, "-"), WELCOME_PARA)
    for number, message in USER_OPTIONS.items():
        print(message.ljust(30, ".") + str(number).rjust(2))

    # main selection loop
    while True:    
        choice = input()
        if choice not in [1, 2, 3, 4, 5, 6]:
            print('Invalid selection\n')
            continue
        else:
            main(choice)
