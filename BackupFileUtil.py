#!python3
# BackupFileUtil.py -- Manage files and directories to store on a backup drive
# INCOMPLETE
# TODO: 1. copy entire file path 2. create class for error handling

from pathlib import Path
import shutil
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug("program start")

# Add and/or manage main program directory
class mainDirConfig:
    def __init__(self, new_path):
        self.new_path = new_path

    def add_main_dir(self) -> None:
        main_dir_config = Path(Path.home()) / "BackupFileUtil"
        if main_dir_config.exists() == False:
            main_dir_config.mkdir()

    def edit_text_file(self) -> None:
        stored_paths = open(Path.home() / "BackupFileUtil\\storedPaths.txt", "a")
        stored_paths.write(self.new_path + "\n")
        stored_paths.close()

class sourceConfig:
    def __init__(self):
        pass

    # View all available storage / optical drives
    @staticmethod
    def return_drives() -> list or str:
        DRIVE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        try:
            return list(
                letter + ":\\" for letter in DRIVE_LETTERS if Path(letter + ":\\").exists()
            )
        except OSError:
            return OS_ERROR_MESSAGE

    # Return existing file paths
    @staticmethod
    def get_paths() -> list:
        stored_paths = open(Path.home() / "BackupFileUtil\\storedPaths.txt", "r")
        path_list = stored_paths.readlines()
        stored_paths.close()
        return path_list

class backupConfig:
    def __init__(self, destination: str, source_list: list) -> None:
        self.destination = destination
        self.source_list = source_list

    # TODO: rewrite to use pathlib instead of shutil
    def overwrite_dir(self, source, dir_to_copy) -> None:
        shutil.copytree(source, self.destination + dir_to_copy, dirs_exist_ok=True)

    def overwrite_files(self, source, file_to_copy) -> None:
        shutil.copy(source, self.destination + file_to_copy)

    # TODO: rewrite to use pathlib instead of os
    def back_up_files(self) -> None:
        for file_path in self.source_list:
            file_path = file_path.strip("\n")
            path_object = Path(file_path)
            if path_object.is_dir() == True:
                self.overwrite_dir(path_object, path_object.name)
            elif (
                    path_object.is_file() == True
                    and Path(self.destination + (path_object.parent.name)).exists() == False
            ):
                Path(self.destination + path_object.parent.name).mkdir()
                self.overwrite_files(
                    path_object,
                    path_object.parent.name + "\\" + path_object.name,
                )
            elif path_object.is_file():
                self.overwrite_files(
                    path_object,
                    path_object.parent.name + "\\" + path_object.name,
                )

def main() -> None:
    # print startup messages
    print("\n", WELCOME_MESSAGE.center(68, "-"), WELCOME_PARA)

    # main selection loop
    while True:
        for number, message in MAIN_MENU.items(): # print main menu
            print(message.ljust(30, ".") + str(number).rjust(2))
        choice = input()
        if choice not in "12345":
            print("Invalid selection\n")
            continue
        match choice:
            case '1': # First time setup
                print(SETUP_MESSAGE)
                while True:
                    path_or_break = input(NEW_PATH_MESSAGE)
                    main_dir_config = mainDirConfig(path_or_break)
                    main_dir_config.add_main_dir()
                    if Path(path_or_break).exists():
                        main_dir_config.edit_text_file()
                    elif path_or_break.lower() == 'b':
                        break
                    else:
                        continue

            case '2': # Add new file path
                while True:
                    path_or_break = input(NEW_PATH_MESSAGE)
                    main_dir_config = mainDirConfig(path_or_break)
                    main_dir_config.add_main_dir()
                    if Path(path_or_break).exists():
                        main_dir_config.edit_text_file()
                    elif path_or_break.lower() == 'b':
                        break
                    else:
                        continue

            case '3': # View existing file paths
                for path in sourceConfig.get_paths():
                    print(path)
                print('\n')

            case '4': # Run Backup
                while True:
                    if type(sourceConfig.return_drives()) == str:
                        print(sourceConfig.return_drives())
                        break
                    elif type(sourceConfig.return_drives()) == list:
                        print(BACKUP_MESSAGE, sourceConfig.return_drives(), BACKUP_WARNING)
                        destination_path = input()
                        if destination_path.lower() == 'b':
                            break
                        elif Path(destination_path).exists() == True:
                            backup_config = backupConfig(destination_path, sourceConfig.get_paths())
                            backup_config.back_up_files()
                            break
                        elif Path(destination_path).exists() == False:
                            print(INVALID_BACKUP_PATH)
                            continue

            case '5': # EXIT
                exit()
                
WELCOME_MESSAGE = " BackupFileUtil "
WELCOME_PARA = """
\nUse this script to store and manage files and directories that you
wish to save to an external drive. If this is a first time setup,
please select 1.\n"""
MAIN_MENU = {
    1: "First time setup",
    2: "Add new file path",
    3: "View existing file paths",
    4: "Run Backup",
    5: "EXIT",
}
SETUP_MESSAGE = """Please enter any file paths you wish to store for
future backups. If path leads to a directory, all files and
subdirectories will be copied to the backup drive. If path
leads to a file, the file will be copied and the parent directory
will be created on the backup drive.\n"""
NEW_PATH_MESSAGE = 'Please enter path, or type "B" to return to main menu.\n'
BACKUP_MESSAGE = (
    "Please enter a path to store your backups. The following drives are available:\n"
)
BACKUP_WARNING = """\n\nWARNING: if you proceed, any files and directories on the backup drive
with the same name as the source drive will be completely overwritten. This cannot be undone!
Type 'b' if you wish to return to the main menu, or enter a path to the backup drive to proceed."""
INVALID_BACKUP_PATH = (
    "Invalid destination path. Please enter a valid file path to store your backups.\n"
)
OS_ERROR_MESSAGE = '''\nWARNING. One of the discovered drives may be corrupt or may be formatted with an invalid
drive type. Please check the volume type of your backup drive(s) before proceeding.\n'''


if __name__ == "__main__":
    main()
