import random
import time
def roll(die):
    print('Rolling...')
    time.sleep(.3)
    for _ in range(times): 								#required for the repeat function
        roll_result.extend([random.randint(1,die)]) 	#extend is used here to drop the results into a list rather than return individual results
    print(roll_result)

roll_result=[] 											# you need to initiate the list before you can extend it
die=int(input("What's your die? "))
times=int(input('How many times? '))


roll(die)

