# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# browser = webdriver.Firefox()
# browser.get('http://nostarch.com')
# htmlElem = browser.find_element_by_tag_name('html')
# htmlElem.send_keys(Keys.END)     # scrolls to bottom
# htmlElem.send_keys(Keys.HOME)    # scrolls to top




# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://mail.yahoo.com')
# emailElem = browser.find_element_by_id('login-username')
# emailElem.send_keys('not_my_real_email')
# passwordElem = browser.find_element_by_id('login-passwd')
# passwordElem.send_keys('12345')
# passwordElem.submit()

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('http://inventwithpython.com')
# linkElem = browser.find_element_by_link_text('Read It Online')
# type(linkElem)
# linkElem.click() # follows the "Read It Online" link


# import webbrowser
# address = input("Gimme an address to Google Map: \n")
# webbrowser.open('https://www.google.com/maps/place/' + address)


# assert False, "This will always assert."

# eggs = "goodbye"
# bacon = "GOODbye"
#
# assert eggs.lower() != bacon.lower(), "Eggs and bacon must not be the same " \
#                                       "(regardless of upper or lower case.)"

# spam = 9
# assert spam >= 10, "Spam must = 10 or more."

# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Start of program')
#
# def factorial(n):
#     logging.debug('Start of factorial(%s)' % (n))
#     total = 1
#     for i in range(n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(%s)' % (n))
#     return total
#
# print(factorial(5))
# logging.debug('End of program')


# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a single character string.')
#     if width <= 2:
#         raise Exception('Width must be greater than 2.')
#     if height <= 2:
#         raise Exception('Height must be greater than 2.')
#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)
#
# for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#     try:
#         boxPrint(sym, w, h)
#     except Exception as err:
#         print('An exception happened: ' + str(err))


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