# A script that renames every file (not including sub-directories) from 1 and increases everytime a file is renamed
# The script will not rename itself
# Be careful running this script! I am not responsible if it causes any damage

import os

# get the current working directory
cwd = os.getcwd()

# get the name of the script file
script_name = os.path.basename(__file__)

# get a list of all files in the current working directory
files = os.listdir(cwd)

# loop through all the files in the current working directory
for i, file in enumerate(files):
    # skip the script file
    if file == script_name:
        continue
    # rename the file using the current loop index and adding 1 to it
    # to start the numbering from 1 instead of 0
    os.rename(file, str(i+1))
