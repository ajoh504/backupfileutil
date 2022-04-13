#!python3
# BackupFileUtil.py -- Manage files and directories to store on a backup drive

from pathlib import Path
import os
import shelve

# TODO: Create .txt file for storing file paths
os.chdir('C:\\Windows\\System32')
storedPaths = open('storedPaths.txt', 'w')

    # TODO: prompt for user input from user options table

# TODO: Create table for user options:

    # First time setup?

    # Select backup drive and source drive

    # Add new file path?

    # View existing filepaths?

    # Configuration (change default .txt location) 


# TODO: Execute commands from user input

    # optionally print existing file paths

    # optionally write to .txt file based on user input

    # optionally backup files

    # optionally display existing file paths or more info
