# import re
#
# test_string = "'Alice eats apples.'" \
#               "'Bob pets cats.'" \
#               "'Carol throws baseballs.'" \
#               "'Alice throws Apples.'" \
#               "'BOB EATS CATS.'" \
#               "but not the following:" \
#               "'Robocop eats apples.'" \
#               "'ALICE THROWS FOOTBALLS.'" \
#               "'Carol eats 7 cats.'"""
#
# test_regex = re.compile(r"(Alice|Bob|Carol) (eats|pets|throws) (apples|baseballs|cats).", re.IGNORECASE)
#
# print(test_regex.findall(test_string))


# import re
#
# test_string = "Satoshi Nakamoto " \
#               "Alice Nakamoto " \
#               "Robocop Nakamoto " \
#               "satoshi Nakamoto " \
#               "Mr. Nakamoto" \
#               "Nakamoto" \
#               "Aa Nakamoto" \
#               "Satoshi nakamoto"
#
#
# test_regex = re.compile(r"[A-Z][a-z]+ Nakamoto")
#
# print(test_regex.findall(test_string))