# BackupFileUtil

### USAGE:

This script allows users to store file paths to a plain text file. The paths can later be used to backup files and directories to an external drive. `shutil.copy()` and `shutil.copytree()` are the methods used for the backup, so running the backup will effectively overwrite the previous files if they already exist on the backup drive. A warning message will be displayed before running the backup, so proceed with caution because this cannot be undone. 

This script takes no command line arguments. All arguments are accepted through `input()` calls.

### GETTING STARTED:

This script was written using Python 3x on Windows. To use this script, a valid Python 3 installation is required. This script will not run on Mac or Linux. Once Python is installed, simply copy and paste the script in the desired location. 

### Run scipt in the command line 

To run the script in the terminal, save the accompanying `.cmd` file with the appropriate file path leading to the `BackupFileUtil.py` script. 

### Run script with Windows Run

To use script with Win + R, add the batch file to 

### CONFIGURATION: 

The script will prompt the user to enter file paths to be stored. The plaintext file is stored by default in the user's home directory, titled `storedPaths.txt`. Optionally, the text file can be edited prior to running the script. To do so, simply open the text file and add file paths with a new line after each path. 
