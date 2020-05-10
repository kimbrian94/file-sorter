import os
import shutil
from sys import argv

# function that takes a directory and sorts it by moving files into 
# each folders according to their extensions
def sortDirectory(directory):
    os.chdir(directory)
    files = os.listdir() # list all files or directories in the directroy and store it in 'files'
    exts = []
    dirs = []
    hasExt = False
    hasFile = False
    hasDir = False
    moved = False

    # create a list of directories in the 'directory' being sorted
    for file in files:
        if os.path.isdir(file):
            dirs.append(file)
            hasDir = True

    # iterate through files and store their extensions in a list
    for file in files:
        split = os.path.splitext(file)
        # check if there is a directory name with the file's extension
        # if there is such directory move the file into that directory
        for dir in dirs:
            if split[1][1:] == dir:
                shutil.move(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), dir))
                print("moving: " + os.path.join(directory, file) + " to: " + os.path.join(directory, dir, file))
                moved = True
        # if file's extension doesn't match any of the directory names
        # then append its extension to the list to be made as directories
        if os.path.isfile(file) and file != '.DS_Store' and moved == False:
            hasFile = True
            for ext in exts:
                if split[1][1:] == ext:
                    hasExt = True
            if hasExt == False:
                exts.append(split[1][1:])
        hasExt = False
    
    # if there are directories but no file, it is already sorted
    if hasFile == False and hasDir == True and moved == False:
        print('This directory is already sorted.')
        exit(0)

    # make new directories with their names as each extensions
    for ext in exts:
        path = os.path.join(os.getcwd(), ext)
        os.mkdir(path)
    
    # move the files into the newly created directories based on their extensions.
    for file in files:
        if os.path.isfile(file) and file != '.DS_Store':
            split = os.path.splitext(file)
            ext = split[1][1:]
            src = os.path.join(os.getcwd(), file)
            dest = os.path.join(os.getcwd(), ext)
            shutil.move(src, dest)
            print("moving: " + os.path.join(directory, file) + " to: " + os.path.join(directory, ext, file))

# main function
def main():
    # take a directory name and pass it to sorting function as its argument 
    if len(argv) == 2:
        print("Running...")
        dirname = argv[1]
        sortDirectory(dirname)
        print("Your directory is now sorted!")
    # prints out if length of argv is not 2
    else:
        print("Please provide directory to be sorted.")
        return 1

if __name__ == '__main__':
    main()