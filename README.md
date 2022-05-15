# BackupFileUtil

### Usage

This script allows users to store file paths to a plain text file. The paths can later be used to backup files and directories to an external drive. `shutil.copy()` and `shutil.copytree()` are the methods used for the backup, so running the backup will effectively overwrite the previous files if they already exist on the backup drive. A warning message will be displayed before running the backup, so proceed with caution because this cannot be undone. 

This script takes no command line arguments. All arguments are accepted through `input()` calls.

If path leads to a directory, all files and subdirectories will be copied to the backup drive. If path leads to a file, the file will be copied and the parent directory will be created on the backup drive.

### Getting Started

This script was written using Python 3.10 on Windows. To use this script, a valid Python 3.10 installation is required. This script will not run on Mac or Linux. Once Python is installed, simply copy and paste the script in the desired location. 

### Run Scipt in the Command Line 

To run the script in the terminal, save the accompanying `.cmd` file with the appropriate file path leading to the `BackupFileUtil.py` script. 

### Optional Configuration

The script will prompt the user to enter file paths to be stored. The plaintext file is stored by default in the user's home directory, titled `storedPaths.txt`. Optionally, the text file can be edited prior to running the script. To do so, simply open the text file and add file paths with a new line after each path. 
