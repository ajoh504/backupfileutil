#!python3
# BackupFileUtil.py -- Manage files and directories to store on a backup drive

from pathlib import Path
import shutil, os

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
leads to a file, the file will becopied and the parent directory
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

# Add main program directory
def add_main_dir() -> None:
    main_dir = Path(Path.home()) / "BackupFileUtil"
    if main_dir.exists() == False:
        main_dir.mkdir()


# Add new file paths
def edit_text_file(new_path) -> None:
    stored_paths = open(Path.home() / "BackupFileUtil\\storedPaths.txt", "a")
    stored_paths.write(new_path + "\n")
    stored_paths.close()


# View all available storage / optical drives
def return_drives() -> list:
    DRIVE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return list(
        letter + ":\\" for letter in DRIVE_LETTERS if Path(letter + ":\\").exists()
    )


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
        file_path = file_path.strip("\n")
        path_object = Path(file_path)
        if path_object.is_dir() == True:
            overwrite_dir(path_object, destination + path_object.name)
        elif (
            path_object.is_file() == True
            and Path(destination + (path_object.parent.name)).exists() == False
        ):
            os.mkdir(destination + path_object.parent.name)
            overwrite_files(
                path_object,
                destination + path_object.parent.name + "\\" + path_object.name,
            )
        elif path_object.is_file():
            overwrite_files(
                path_object,
                destination + path_object.parent.name + "\\" + path_object.name,
            )


def main() -> None:
    # print startup messages
    print("\n", WELCOME_MESSAGE.center(68, "-"), WELCOME_PARA)

    # main selection loop
    while True:
        for number, message in MAIN_MENU.items():
            print(message.ljust(30, ".") + str(number).rjust(2))  # print main menu
        choice = input()
        if choice not in "12345":
            print("Invalid selection\n")
            continue
        match choice:
            case '1': # First time setup
                add_main_dir()
                print(SETUP_MESSAGE)
                while True:
                    path_or_break = input(NEW_PATH_MESSAGE)
                    if Path(path_or_break).exists():
                        edit_text_file(path_or_break)
                    elif path_or_break.lower() == 'b':
                        break
                    else:
                        continue
            case '2': # Add new file path
                while True:
                    path_to_add = input(NEW_PATH_MESSAGE)
                    if Path(path_to_add).exists():
                        edit_text_file(path_to_add)
                    elif path_to_add.lower() == 'b':
                        break
                    else:
                        continue
            case '3': # View existing file paths
                for path in get_paths():
                    print(path)
                print('\n')
            case '4': # Run Backup
                while True:
                    print(BACKUP_MESSAGE, return_drives(), BACKUP_WARNING)
                    destination_path = input()
                    if destination_path.lower() == 'b':
                        break                    
                    elif Path(destination_path).exists() == True:
                        back_up_files(get_paths(), destination_path)
                        break
                    elif Path(destination_path).exists() == False:
                        print(INVALID_BACKUP_PATH)
                        continue

            case '5': # EXIT
                exit()


if __name__ == "__main__":
    main()
