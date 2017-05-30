import os

# Deleting Unneeded Files practice from Automate The Boring Stuff
# It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard
# drive. If you’re trying to free up room on your computer, you’ll get the most bang for your buck by deleting the most
# massive of the unwanted files. But first you have to find them.
# Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that
# have a file size of more than 100MB. (Remember, to get a file’s size, you can use os.path.getsize() from the os
# module.) Print these files with their absolute path to the screen.

targeted_directory = "C:\\Users\\LB\\Desktop\\PythonProjects\\AutomateTheBoringStuffProjects\\shutil_tests"

print("Files over 1MB:") # Using 1MB for the sake of testing, includes more files.

for filenames in os.walk(targeted_directory):
    for filename in filenames[2]:
        if os.path.getsize(targeted_directory + "\\" + filename) > 1048576:
            print(filename)
            print(str(round(os.path.getsize(targeted_directory + "\\" + filename) / 1048576, 2)) + " MB")
