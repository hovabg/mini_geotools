#!/usr/bin/env python3

import sys, getopt
from os import listdir
from os.path import isfile, join


def main(argv):

    try:
        opts, args = getopt.getopt(argv, "p:", ["path="])
    except getopt.GetoptError:
        sys.exit(2)

    path = './'

    for opt, arg in opts:
        if opt in ['-p', '--path']:
            path = arg

    check_files(path)


def check_files(path):
    # Mandatory extensions
    extensions = ['t2']

    files = {}
    # Iterate files in given path
    for file in listdir(path):
        # Check for files only (avoid processing directories)
        if isfile(join(path, file)):
            # Split filename by dot to get extension
            parts = file.lower().split('.')
            file_name = parts[0]
            file_ext = parts[-1]

            # If the file extension is on one of the listed extensions
            if file_ext in extensions:
                # Create a dictionary for each file, adding the found extension
                if file_name not in files:
                    files[file_name] = []
                files[file_name].append(file_ext)

    # Flag to control errors
    errors = False

    # Iterate over all found files
    for key, values in files.items():
        # Iterate all over mandatory extensions
        for ext in extensions:
            # If the mandatory extension is not in the files throw an error
            if ext not in values:
                errors = True
                print("File group " + key + " is missing its " + ext + " file")

    # If no errors were found
    if not errors:
        print("OK, the following files were validated:")
        for file in files:
            print("- " + file)


if __name__ == "__main__":
    main(sys.argv[1:])
