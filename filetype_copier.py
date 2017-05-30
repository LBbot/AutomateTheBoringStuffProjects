import shutil, os

#Selective Copy practice from Automate The Boring Stuff
# Write a program that walks through a folder tree and searches for files with a certain file extension (such as
# .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

# Editable fields:
targeted_directory = "C:\\Users\\LB\\Desktop\\PythonProjects\\AutomateTheBoringStuffProjects\\shutil_tests"
copy_directory = "C:\\Users\\LB\\Desktop\\PythonProjects\\AutomateTheBoringStuffProjects\\shutil_tests\\copyfolder"
file_type = ".png"

for filenames in os.walk(targeted_directory):
    for filename in filenames[2]:
        if filename.endswith(file_type):
            print(filename)
            shutil.copy(targeted_directory + "\\" + filename, copy_directory)
