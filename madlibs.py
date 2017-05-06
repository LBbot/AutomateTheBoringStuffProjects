# my_file = open("madlibs.txt", "r")
# filereader = my_file.read()
#
# word1 = input("Enter an adjective:\n")
# word2 = input("Enter noun:\n")
# word3 = input("Enter verb (past tense!):\n")
# word4 = input("Enter noun:\n")
#
# filereader = filereader.replace("ADJECTIVE", word1)
# filereader = filereader.replace("NOUN", word2, 1)
# filereader = filereader.replace("VERB", word3)
# filereader = filereader.replace("NOUN", word4)
#
# with open("madlibsoutput.txt", "w") as file:
#     file.write(filereader)

my_file = open("madlibs.txt", "r")
filereader = my_file.read()

word1 = input("Enter an adjective:\n")
word2 = input("Enter noun:\n")
word3 = input("Enter verb (past tense!):\n")
word4 = input("Enter noun:\n")

for word in ["ADJECTIVE", "NOUN", "VERB"]:
        filereader = filereader.replace(word, "{}")

filereader = filereader.format(word1, word2, word3, word4)

with open("madlibsoutput.txt", "w") as file:
    file.write(filereader)
