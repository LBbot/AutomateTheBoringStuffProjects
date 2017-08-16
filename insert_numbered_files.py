#!bin/env python3
# Filling in the Gaps practice question from Automate The Boring Stuff:
# "[Previous challenge info: Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt,
# and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt
#  but no spam002.txt). Have the program rename all the later files to close this gap.]
# As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added."

import os
import math

targeted_directory = "C:\\Users\\LB\\Desktop\\PythonProjects\\AutomateTheBoringStuffProjects\\shutil_tests"
new_file = "test0005.txt"  # This is where you want to create the gap.

for root, dirs, files in os.walk(targeted_directory):
    if new_file in files:
        for filename in reversed(files):
            if filename.endswith(".txt"):
                past_zeroes_flag = False
                old_number = []

                for letter in filename:
                    try:
                        if int(letter) > 0:
                            past_zeroes_flag = True
                    except ValueError:
                        continue

                    if past_zeroes_flag:
                        try:
                            int(letter)
                            old_number.append(letter)
                        except ValueError:
                            continue

                old_number = "".join(old_number)
                if len(old_number) < len(str(int(old_number) + 1)):
                    old_number = "0" + old_number
                rename = filename.replace(old_number, str(int(old_number) + 1))
                print("Renaming {} to {}".format(filename, rename))

                os.rename(targeted_directory + "\\" + filename, targeted_directory + "\\" + rename)

                if filename == new_file:
                    break

# Can replace line 13 with the following to "save an indent":
# if new_file not in files:
#     continue
