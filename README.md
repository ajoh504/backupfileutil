# backupfileutil

### Usage

This script allows users to store file paths to a plain text file. The paths can later be used to backup files and directories to an external drive. Each new backup is created with the directory name "backup" followed by a date and time stamp. Previous backups will not be overwritten unless the user chooses to delete them manually. 

This script takes no command line arguments. All arguments are accepted through `input()` calls.

If the given path leads to a directory, all files and subdirectories will be copied to the backup drive, and the directory's parents will be created on the backup drive. If the path leads to a file, the file will be copied and the parents will be created on the backup drive.

### Requirements

This script was written using Python 3.10 on Windows. To use this script, a valid Python 3.10 installation is required. This script has not been tested on macOS or Linux. 

### Optional Configuration

During the first time setup, the script will prompt the user to enter file paths to be stored. A directory called "backupfileutil" will be created in the user's home directory. The plain text file, titled `storedpaths.txt`, is stored there by default. Optionally, the text file can be edited prior to running the backup. To do so, simply open the text file and add file paths with a new line after each path. 
