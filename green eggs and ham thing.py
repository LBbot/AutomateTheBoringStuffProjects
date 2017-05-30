# f = open("text.txt", "rb")
# s = f.readlines()
# f.close()
# f = open("newtext.txt", "wb")
# s.reverse()
# for item in s:
#   print>>f, item
# f.close()


# my_file = open("newtext.txt", "wb")

# count = 0

# for item in s:
#     if item == "i ":
#         newitem = item = "I "
#         my_file.write(newitem)
#         count += 1
#     if item == "i-":
#         newitem = item = "I-"
#         my_file.write(newitem)
#         count += 1
#     else:
#         my_file.write(item)
#     print(count)
# my_file.close()


#filereader = filereader.replace("i ", "I ")
#filereader2 = filereader.replace("i-", "I-")

# with open('newtext.txt', 'w') as file:
#     file.write(filereader2)


# my_file = open("Green Eggs and Ham.txt", "r")
# filereader = my_file.read()
# my_file.close()
#
# spacecount = 0
# dashcount = 0
#
# def i_check(thingy):
#     if thingy == "i ":
#         return True
#     else:
#         return False
#
# def i_dash_check(thingy):
#     if thingy == "i-":
#         return True
#     else:
#         return False
#
# for lettur in range(len(filereader)):
#     chunk = filereader[lettur:lettur+2]
#     if i_check(chunk):
#         filereader2 = filereader.replace(chunk, "I ")
#         spacecount += 1
#         print(spacecount)
#     if i_dash_check(chunk):
#         filereader3 = filereader.replace(chunk, "I-")
#         dashcount += 1
#         print(dashcount)
#         with open('newtext.txt', 'w') as file:
#             file.write(filereader3)
#
# print("Totals under here:")
# print(spacecount)
# print(dashcount)
# totalcount = spacecount + dashcount
# print(totalcount)


# import re
# my_file = open("Green Eggs and Ham.txt", "r")
# filereader = my_file.read()
# my_file.close()
#
# # space_regex = re.compile(r"i ")
# # dash_regex = re.compile(r"i-")
#
# # print("Errors fixed: " + str(len(space_regex.findall(filereader)) + len(dash_regex.findall(filereader))))
#
# # filereader = space_regex.sub(r"I ", filereader)
# # filereader = dash_regex.sub(r"I-", filereader)
#
# with open("newtext.txt", "w") as file:
#     file.write(filereader)


import re
my_file = open("Green Eggs and Ham.txt", "r")
filereader = my_file.read()
my_file.close()

i_regex = re.compile(r"i( |-)")

print("Errors fixed: " + str(len(i_regex.findall(filereader))))

filereader = i_regex.sub(r"I\1", filereader)

with open("newtext.txt", "w") as file:
    file.write(filereader)
