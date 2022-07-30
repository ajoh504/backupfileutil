#!python3
# backupfileutil.py -- Manage files and directories to store on a backup drive



import shutil
import os
import json
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
        shutil.copytree(
            dir_path,
            self.destination + "/".join(Path(dir_path).parts[1:]),
            dirs_exist_ok=True,
        )

    def copy_files(self, file_path: str) -> None:
        shutil.copy(file_path, self.destination + "/".join(Path(file_path).parts[1:-1]))

    def back_up_files(self) -> None:
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


def edit_text_file(new_path: str) -> None:  # edit text file containing file paths
    with open(Path.home() / "backupfileutil/storedpaths.txt", "a") as stored_paths:
        stored_paths.write(new_path + "\n")


def add_main_dir() -> None:  # add "backupfileutil" to the User's home directory
    main_dir = Path(Path.home()) / "backupfileutil"
    if main_dir.exists() == False:
        main_dir.mkdir()


# TODO: return joined list with spaces and numbered elements for each drive
def return_drives() -> str:  # return all available storage media
    DRIVE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return " ".join(
        [letter + ":/" for letter in DRIVE_LETTERS if Path(letter + ":/").exists()]
    )


def get_paths() -> list:  # return a list of all stored file paths
    stored_paths = open(Path.home() / "backupfileutil/storedpaths.txt", "r")
    path_list = stored_paths.readlines()
    stored_paths.close()
    return path_list


def get_json_data() -> dict:
    with open("text.json", "r") as json_file:
        return json.load(json_file)


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
                    edit_text_file(choice)
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
