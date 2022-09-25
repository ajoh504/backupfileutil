#!python3
# backupfileutil.py -- Manage files and directories to store on a backup drive


import shutil
import os
import json
from pathlib import Path
from datetime import datetime


def copy_tree(destination: str, dir_path: str) -> None:
    """Copy directory and all of its files and subdirectories to destination drive."""
    shutil.copytree(
        dir_path,
        destination + "/".join(Path(dir_path).parts[1:]),
        dirs_exist_ok=True,
    )


def copy_files(destination: str, file_path: str) -> None:
    """Copy files to destination drive."""
    shutil.copy(file_path, destination + "/".join(Path(file_path).parts[1:-1]))


def back_up_files(destination: str, file_list: str) -> None:
    """
    Run the main backup script by looping through the paths from storedpaths.txt. If
    file_path is a directory, then copy all of its files and subdirectories to the
    backup folder. If file_path is a file, check to make sure its parent directories
    exist on the destination drive. If parents do not exist, create them on the
    destination drive and copy the file. Lastly, copy any remaining files from the
    source_list.
    """
    for file_path in file_list:
        file_path = file_path.strip("\n")
        if Path(file_path).is_dir() == True:
            copy_tree(destination, file_path)
        elif (
            Path(file_path).is_file() == True
            and Path(destination + "/".join(Path(file_path).parts[1:-1])).exists()
            == False
        ):
            os.makedirs(destination + "/".join(Path(file_path).parts[1:-1]))
            copy_files(destination, file_path)
        elif Path(file_path).is_file():
            copy_files(destination, file_path)


def edit_text_file(new_path: str) -> None:
    """edit text file containing file paths"""
    with open(Path.home() / "backupfileutil/storedpaths.txt", "a") as stored_paths:
        stored_paths.write(new_path + "\n")


def add_main_dir() -> None:
    """add "backupfileutil" to the User's home directory"""
    main_dir = Path(Path.home()) / "backupfileutil"
    if main_dir.exists() == False:
        main_dir.mkdir()


def return_drives() -> str:
    """Return all available storage media"""
    DRIVE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return " ".join(
        [letter + ":/" for letter in DRIVE_LETTERS if Path(letter + ":/").exists()]
    )


def get_paths() -> list:
    """Return a list of all stored file paths"""
    with open(Path.home() / "backupfileutil/storedpaths.txt", "r") as stored_paths:
        return stored_paths.readlines()


def get_json_data() -> dict:
    with open(f"{Path.cwd()}/text.json", "r") as json_file:
        return json.load(json_file)


def main():
    add_main_dir()
    TEXT = get_json_data()

    """Print startup messages"""
    print("\n", TEXT["WELCOME"].center(82, "-"), "\n".join(TEXT["WELCOME_PARA"]))

    while True:
        for number, message in TEXT["MAIN_MENU"].items():  # print main menu
            print(message.ljust(30, ".") + str(number).rjust(2))
        choice = input()
        if choice not in "1234":
            print("Invalid selection\n")
            continue
        elif choice == "1":
            while True:
                choice = input(TEXT["NEW_PATH"])
                if Path(choice).exists():
                    edit_text_file(choice)
                elif choice.lower() == "b":
                    break
                else:
                    continue

        elif choice == "2":
            for path in get_paths():
                print(path)

        elif choice == "3":
            while True:
                try:
                    print(
                        TEXT["BACKUP"],
                        return_drives(),
                    )
                    destination_drive = input()
                    if destination_drive.lower() == "b":
                        break
                    elif (
                        Path(destination_drive).exists() == True
                        and destination_drive != ""
                    ):
                        destination_drive = f"{destination_drive}backup_{datetime.now().strftime('%Y%m%d%H%M%S')}/"
                        print("\nBackup in progress. Please wait.\n")
                        back_up_files(destination_drive, get_paths())
                        print("\nBackup complete.\n")
                        break
                    elif Path(destination_drive).exists() == False:
                        print(TEXT["INVALID_BACKUP_PATH"])
                        continue
                except OSError:
                    print(return_drives(), TEXT["OS_ERROR"])

        elif choice == "4":
            exit()


if __name__ == "__main__":
    main()
