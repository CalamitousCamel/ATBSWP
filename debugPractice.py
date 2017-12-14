import random
import logging
logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('start program')
guess = ''
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
logging.debug('toss is ' + str(toss))
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()

if toss == 1 and guess in 'heads':
    print('You got it!')
elif toss == 0 and guess in 'tails':
    print('You got it!')
else:
    print('Nope! Guess again!')
    logging.debug('input guess: ' + guess)
    logging.debug(str(toss))
    guess = input().lower()
    logging.debug('second guess: ' + guess)
    if toss == 1 and guess in 'heads':
        print('You got it!')
    elif toss == 0 and guess in 'tails':
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
