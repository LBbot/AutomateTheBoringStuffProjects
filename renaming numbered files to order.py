import os, math

# Filling in the Gaps practice from Automate The Boring Stuff
# Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single
# folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
# Have the program rename all the later files to close this gap.
# As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.

targeted_directory = "C:\\Users\\LB\\Desktop\\PythonProjects\\AutomateTheBoringStuffProjects\\shutil_tests"

count = 1

for filenames in os.walk(targeted_directory):
    for filename in filenames[2]:
        if filename.endswith(str(count) + ".txt"):
            print(filename + " is correctly numbered")
            count += 1
            # print(count) # for testing
        elif filename.endswith(".txt"):
            minuscharacter = int(math.log10(count)+1) + 4   # ALTERNATIVELY: len(str(count)) + 4
            new_file_name = targeted_directory + "\\" + filename[:-minuscharacter] + str(count) + ".txt"
            print(filename + " will be renamed " + new_file_name)
            os.rename(targeted_directory + "\\" + filename, new_file_name)
            count += 1
            # print(count) # for testing
