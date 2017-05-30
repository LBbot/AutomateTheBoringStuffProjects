stringinput = input("Type your name and press enter, and I will make it look fancy in a '90s way.\n")
bannerlength = "*" * len(stringinput) + "*" * 4
print(bannerlength + "\n* " + stringinput + " *\n" + bannerlength)