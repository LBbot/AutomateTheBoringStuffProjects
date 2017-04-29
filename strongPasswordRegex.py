import re

#TEST INPUTS
#inputt = "Aliceeatsapples1"
#inputt = "123456789Ab"
#inputt = "12345678"
#inputt = "abc"
#inputt = "Abcdefgh"
#inputt = "abcdefgh"

while True:
    inputt = input("Please enter a password. It must be at least 8 characters long, contain at least one number and a mix of uppercase and lowercase letters. \n")

    # TM's MASTER REGEX
    tm_regex = re.compile(r"^(?:([a-z])|([A-Z])|([0-9])|.){8,64}$")

    try:
        if tm_regex.search(inputt).group(1) and tm_regex.search(inputt).group(2) and tm_regex.search(inputt).group(3):
            print("Password accepted.")
            break
        else:
            print("Your password MUST contain a at least one number and a mix of uppercase and lowercase letters.")
    except AttributeError:
        print("Your password MUST be at least 8 characters long.")


    # VERSION DOING IT THE LONG WAY
    # password_regex1 = re.compile(r".{8,}")
    # password_regex2 = re.compile(r"[A-Z]+")
    # password_regex3 = re.compile(r"[a-z]+")
    # password_regex4 = re.compile(r"[0-9]+")
    #
    # check1 = password_regex1.findall(inputt)
    # check2 = password_regex2.findall(inputt)
    # check3 = password_regex3.findall(inputt)
    # check4 = password_regex4.findall(inputt)
    #
    # if check1 and check2 and check3 and check4:
    #     print("Password accepted.")
    #     break
    # else:
    #     print("Your password MUST be at least 8 characters long and contain at least one number and a mix of uppercase and "
    #           "lowercase letters.")
