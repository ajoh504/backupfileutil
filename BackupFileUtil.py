#!python3
# BackupFileUtil.py -- Manage files and directories to store on a backup drive

from pathlib import Path
import os
import shelve


def main():
    # TODO: prompt for user input from user options table
    input()
    # Retrieve user home directory, check if BackupFileUtil dir exists
    newDir = Path(Path.home()) / "BackupFileUtil"
    if newDir.exists() == False:
        os.makedirs(newDir)

    # Create .txt file for storing file paths
    os.chdir(Path(Path.home()) / "BackupFileUtil")
    storedPaths = open("storedPaths.txt", "w")

    # TODO: Execute commands from user input

    # optionally print existing file paths

    # optionally write to .txt file based on user input

    # optionally backup files

    # optionally display existing file paths or more info


if __name__ == "__main__":
    WELCOME_MESSAGE = " Welcome to BackupFileUtil v. 1.0 "
    WELCOME_PARA = """
\nUse this script to store and manage files and directories that you
wish to save to an external drive. If this is a first time setup,
please select 1 for easy setup or 2 to configure the default script
file locations.\n"""
    USER_OPTIONS = {
        1: "First time setup: easy",
        2: "First time setup: advanced",
        3: "Add new file path",
        4: "View existing filepaths",
        5: "About",
    }

    print(WELCOME_MESSAGE.center(68, "-"), WELCOME_PARA)
    for number, message in USER_OPTIONS.items():
        print(message.ljust(30, ".") + str(number).rjust(2))
    while True:    
        main(input())
