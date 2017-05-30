import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

import random
guess = ''
while guess.lower() not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 1:
    toss = "heads"
else:
    toss = "tails"

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program')

# ORIGINAL FROM BOOK:

# import random
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()
# toss = random.randint(0, 1) # 0 is tails, 1 is heads
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guesss = input()
#     if toss == guess:
#        print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')
