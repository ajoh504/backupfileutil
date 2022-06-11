# !python3
# BackupFileUtil.py -- Manage files and directories to store on a backup drive
# TODO: create class for error handling
# TODO: shorten main() function / search for reusable code

from pathlib import Path
import shutil
import os
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug("Program start")


class mainDirConfig:  # Add and/or manage main program directory
    def __init__(self, new_path):
        self.new_path = new_path

    def add_main_dir(self) -> None:  # add "BackupFileUtil" to the User's home directory
        main_dir_config = Path(Path.home()) / "BackupFileUtil"
        if main_dir_config.exists() == False:
            main_dir_config.mkdir()

    def edit_text_file(self) -> None:  # edit text file containing file paths
        stored_paths = open(Path.home() / "BackupFileUtil/storedPaths.txt", "a")
        stored_paths.write(self.new_path + "\n")
        stored_paths.close()


class sourceConfig:
    def __init__(self):
        pass

    # TODO: return joined list with spaces and numbered elements for each drive
    @staticmethod
    def return_drives() -> str:  # return all available storage media
        DRIVE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ' '.join([letter + ":/" for letter in DRIVE_LETTERS if Path(letter + ":/").exists()])

    @staticmethod
    def get_paths() -> list:  # return a list of all stored file paths
        stored_paths = open(Path.home() / "BackupFileUtil/storedPaths.txt", "r")
        path_list = stored_paths.readlines()
        stored_paths.close()
        return path_list


class backupConfig:
    def __init__(self, destination: str, source_list: list) -> None:
        self.destination = destination + 'Backups/'  # dir named 'Backups' on destination drive
        self.source_list = source_list

    def copy_tree(self, dir_path: str) -> None:
        shutil.copytree(dir_path, self.destination + '/'.join(Path(dir_path).parts[1:]), dirs_exist_ok=True)

    def copy_files(self, file_path: str) -> None:
        shutil.copy(file_path, self.destination + '/'.join(Path(file_path).parts[1:-1]))

    def back_up_files(self) -> None:
        for file_path in self.source_list:
            file_path = file_path.strip("\n")
            if Path(file_path).is_dir() == True:
                self.copy_tree(file_path)
            elif (
                    Path(file_path).is_file() == True
                    and Path(self.destination + '/'.join(Path(file_path).parts[1:-1])).exists() == False
            ):
                os.makedirs(self.destination + '/'.join(Path(file_path).parts[1:-1]))
                self.copy_files(file_path)
            elif Path(file_path).is_file():
                self.copy_files(file_path)

def consume_new_path() -> None:
    while True:
        choice = input(NEW_PATH_MESSAGE)
        main_dir_config = mainDirConfig(choice)
        main_dir_config.add_main_dir()
        if Path(choice).exists():
            main_dir_config.edit_text_file()
        elif choice.lower() == 'b':
            break
        else:
            continue

def main() -> None:
    print("\n", WELCOME_MESSAGE.center(82, "-"), WELCOME_PARA)  # print startup messages
    while True:  # main selection loop
        for number, message in MAIN_MENU.items():  # print main menu
            print(message.ljust(30, ".") + str(number).rjust(2))
        main_menu_choice = input()
        if main_menu_choice not in "123456":
            print("Invalid selection\n")
            continue
        match main_menu_choice:
            case '1':  # First time setup
                print(SETUP_MESSAGE)
                consume_new_path()
                continue

            case '2':  # Add new file path
                consume_new_path()
                continue

            case '3':  # View existing file paths
                for path in sourceConfig.get_paths():
                    print(path)

            case '4':  # Run Backup
                while True:
                    try:
                        print(BACKUP_MESSAGE, sourceConfig.return_drives(), BACKUP_WARNING)
                        case_four_choice = input()
                        if case_four_choice.lower() == 'b':
                            break
                        elif Path(case_four_choice).exists() == True and case_four_choice != '':
                            backup_config = backupConfig(case_four_choice, sourceConfig.get_paths())
                            backup_config.back_up_files()
                            break
                        elif Path(case_four_choice).exists() == False:
                            print(INVALID_BACKUP_PATH)
                            continue
                    except OSError:
                        print(sourceConfig.return_drives(), OS_ERROR_MESSAGE)

            case '5':  # view README
                print(README)

            case '6': # end program
                exit()


WELCOME_MESSAGE = " BackupFileUtil "
WELCOME_PARA = """
\nUse this script to store and manage files and directories that you wish to save to 
an external drive. If this is a first time setup, please select 1.\n"""
MAIN_MENU = {
    1: "First time setup",
    2: "Add new file path",
    3: "View existing file paths",
    4: "Run Backup",
    5: "README",
    6: "EXIT"
}
SETUP_MESSAGE = """
Please enter a path to any file you wish to store for future backups. Directory paths 
will be copied with all files and subdirectories.\n"""
NEW_PATH_MESSAGE = "Please enter a file path, or type 'B' to return to main menu.\n"
BACKUP_MESSAGE = "\nPlease type in a drive location to store your backups. The following drives are available:\n"
BACKUP_WARNING = """
\nWARNING: if you proceed, any files and directories on the backup drive with the same 
name as the source drive will be completely overwritten. This cannot be undone! Type 'B' 
if you wish to return to the main menu, or type in a backup drive letter to proceed.\n"""
INVALID_BACKUP_PATH = "Invalid destination path. Please enter a valid file path to store your backups."
OS_ERROR_MESSAGE = '''
\nWARNING. One of the discovered drives may be corrupt or may be formatted with an invalid
drive type. Please check the volume type of your backup drive(s) before proceeding.\n'''
README = '''
BackupFileUtil README

----- Usage -----

This script allows users to store file paths to a plain text file. The paths can later be used 
to backup files and directories to an external drive. `shutil.copy()` and `shutil.copytree()` 
are the methods used for the backup, so running the backup will effectively overwrite the 
previous files if they already exist on the backup drive. A warning message will be displayed 
before running the backup, so proceed with caution because this cannot be undone. 

This script takes no command line arguments. All arguments are accepted through `input()` calls.

If the given path leads to a directory, all files and subdirectories will be copied to the 
backup drive, and the directory's parents will be created on the backup drive. If the path 
leads to a file, the file will be copied and the parents will be created on the backup drive.

----- Requirements -----

This script was written using Python 3.10 on Windows. To use this script, a valid Python 3.10 
installation is required. This script has not been tested on macOS or Linux. 

----- Optional Configuration -----

During the first time setup, the script will prompt the user to enter file paths to be stored. 
A directory called "BackupFileUtil" will be created in the user's home directory. The plain 
text file, titled `storedPaths.txt`, is stored there by default. Optionally, the text file can 
be edited prior to running the backup. To do so, simply open the text file and add file paths 
with a new line after each path. 
'''

if __name__ == "__main__":
    main()
