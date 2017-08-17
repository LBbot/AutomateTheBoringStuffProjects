#!bin/env python3
# make_gap_in_numbered_files.py - can look at a range of numbered files in a directory and rename them to create a gap
# in the ordering for a new file in the middle. (For example if the user had "photo01.jpg, photo02.jpg, photo03.jpg and
#  photo04.jpg" and wanted a new photo to be second in that order it would change 02 to 03 and so on and so on - to
# accomodate that.)
# Filling in the Gaps practice question from "Automate The Boring Stuff".

import os

targeted_directory = "C:\\Users\\LB\\Desktop\\PythonProjects\\AutomateTheBoringStuffProjects\\shutil_tests"
new_file = "test0005.txt"  # This is where you want to create the gap.

for root, dirs, files in os.walk(targeted_directory):
    if new_file in files:
        for filename in reversed(files):
            if filename.endswith(".txt"):  # Correct extension needs to go here.
                past_zeroes_flag = False
                old_number = []

                # Loops through every character in filename until it finds the first number higher than zero.
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

                # Turn [1, 2, 3] into 123
                old_number = "".join(old_number)

                # 9 needs to be "09" or will add a new character when searched for as string and replaced with +1.
                if len(old_number) < len(str(int(old_number) + 1)):
                    old_number = "0" + old_number

                rename = filename.replace(old_number, str(int(old_number) + 1))
                print("Renaming {} to {}".format(filename, rename))

                os.rename(targeted_directory + "\\" + filename, targeted_directory + "\\" + rename)

                if filename == new_file:
                    break


# Can replace line 15 with the following to save an indent, but add a line and lose clarity:
# if new_file not in files:
#     continue
