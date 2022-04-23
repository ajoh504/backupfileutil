#!python3
# BackupFileUtil.py -- Manage files and directories to store on a backup drive

from pathlib import Path
import os, shelve

class setup:
    def __init__(self):
        pass
    # Retrieve user's home directory, check if BackupFileUtil dir exists
    def add_main_dir():
        new_dir = Path(Path.home()) / "BackupFileUtil"
        if new_dir.exists() == False:
            os.makedirs(new_dir)
        
    # Create .txt file for storing file paths
    def create_text_file():
        os.chdir(Path(Path.home()) / "BackupFileUtil")
        storedPaths = open("storedPaths.txt", "w")

    def store_paths():
        
def main(user_input):
    # TODO: Execute commands from user input
    if user_input == 1:
        pass
        
    # optionally print existing file paths

    # optionally write to .txt file based on user input

    # optionally backup files

    # optionally display existing file paths or more info


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
        if choice not in [1, 2, 3, 4, 5]:
            print('Invalid selection\n')
            continue
        else:
            main(choice)

