my_file = open("Green Eggs and Ham.txt", "r")
filereader = my_file.read()
my_file.close()

count = 0

targetlist = ["i ", "i-"]
# Using a variable so you can easily add better grammatical definitions for the word I.

for letter in range(len(filereader)):
    chunk = filereader[letter:letter+2]
    if chunk in targetlist:
        count += 1
        print("Errors fixed: " + (str(count)))
        chunk = chunk.upper()

for letter in range(len(filereader)):
    chunk = filereader[letter:letter+2]
    if chunk in targetlist:
        filereader = filereader.replace(chunk, chunk.upper())

with open("newtextnoregex.txt", "w") as file:
    file.write(filereader)