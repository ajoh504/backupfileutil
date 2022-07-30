#!python3
# backupfileutil.py -- Manage files and directories to store on a backup drive



import shutil
import os
import json
import sys
from pathlib import Path
from datetime import datetime
import logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s -  %(levelname)s -  %(message)s"
)
logging.debug("Program start")


class Backup:
    def __init__(self, destination: str, source_list: list):
        self.destination = (
            f"{destination}backups_{datetime.now().strftime('%Y%m%d%H%M%S')}/"
        )
        self.source_list = source_list

    def copy_tree(self, dir_path: str) -> None:
        """Copy directory and all of its files and subdirectories to destination drive."""
        shutil.copytree(
            dir_path,
            self.destination + "/".join(Path(dir_path).parts[1:]),
            dirs_exist_ok=True,
        )

    def copy_files(self, file_path: str) -> None:
        """Copy files to destination drive."""
        shutil.copy(file_path, self.destination + "/".join(Path(file_path).parts[1:-1]))

    def back_up_files(self) -> None:
        """
        Run the main backup script by looping through the paths from storedpaths.txt. If
        file_path is a directory, then copy all of its files and subdirectories to the
        backup folder. If file_path is a file, check to make sure its parent directories
        exist on the destination drive. If parents do not exist, create them on the
        destination drive and copy the file. Lastly, copy any remaining files from the
        source_list.
        """
        for file_path in self.source_list:
            file_path = file_path.strip("\n")
            if Path(file_path).is_dir() == True:
                self.copy_tree(file_path)
            elif (
                Path(file_path).is_file() == True
                and Path(
                    self.destination + "/".join(Path(file_path).parts[1:-1])
                ).exists()
                == False
            ):
                os.makedirs(self.destination + "/".join(Path(file_path).parts[1:-1]))
                self.copy_files(file_path)
            elif Path(file_path).is_file():
                self.copy_files(file_path)


def add_new_path(new_path: str) -> None:
    """Add new path to storedpaths.txt."""
    with open(Path.home() / "backupfileutil/storedpaths.txt", "a") as stored_paths:
        stored_paths.write(new_path + "\n")


def add_main_dir() -> None:
    """Add dir 'backupfileutil' to  User's home directory."""
    main_dir = Path(Path.home()) / "backupfileutil"
    if main_dir.exists() == False:
        main_dir.mkdir()


def return_drives() -> str:
    """:return str: Return available Windows drive letters to store backups to."""
    DRIVE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return " ".join(
        [letter + ":/" for letter in DRIVE_LETTERS if Path(letter + ":/").exists()]
    )


def get_paths() -> list:
    """Return a list of all stored file paths."""
    with open(Path.home() / "backupfileutil/storedpaths.txt", "r") as paths:
        return paths.readlines()


def get_json_data() -> dict:
    '''
    Get the absolute path to the file text.json and open it.

    :return dict: Text.json contains all script messages to be printed.
    '''
    json_file = str(Path(sys.argv[0]).parent / "text.json")
    with open(json_file, "r") as j:
        return json.load(j)


def main() -> None:
    add_main_dir()
    TEXT = get_json_data()
    print(
        "\n", TEXT["WELCOME"].center(82, "-"), "\n".join(TEXT["WELCOME_PARA"])
    )  # print startup messages
    while True:  # main selection loop
        for number, message in TEXT["MAIN_MENU"].items():  # print main menu
            print(message.ljust(30, ".") + str(number).rjust(2))
        main_menu_choice = input()
        if main_menu_choice not in "1234":
            print("Invalid selection\n")
            continue
        elif main_menu_choice == "1":
            while True:
                choice = input(TEXT["NEW_PATH"])
                if Path(choice).exists():
                    add_new_path(choice)
                elif choice.lower() == "b":
                    break
                else:
                    continue
        elif main_menu_choice == "2":
            for path in get_paths():
                print(path)
        elif main_menu_choice == "3":
            while True:
                try:
                    print(
                        TEXT["BACKUP"],
                        return_drives(),
                    )
                    case_four_choice = input()
                    if case_four_choice.lower() == "b":
                        break
                    elif (
                        Path(case_four_choice).exists() == True
                        and case_four_choice != ""
                    ):
                        Backup(case_four_choice, get_paths()).back_up_files()
                        break
                    elif Path(case_four_choice).exists() == False:
                        print(TEXT["INVALID_BACKUP_PATH"])
                        continue
                except OSError:
                    print(return_drives(), TEXT["OS_ERROR"])

        elif main_menu_choice == "4":
            exit()

if __name__ == "__main__":
    main()
