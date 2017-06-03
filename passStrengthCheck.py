#! Python3
import random
'''TODO:
give password instructions
accept user input
test password
	for 8 char
	for U & u letters
	for at least 1 digit
respond accordingly
accept user input'''

testPasslist= [r'9!Products!Taken!2',
			'8%Broke%Neighbor%6',
			'8:Members:Southern:9',
			'8&Planet&Home&7',
			'0;Industry;Wheels;2',
			'1@Inch@Plane@6',
			'4?Chance?Science?9',
			'4_Spent_Round_4',
			'5/August/Head/2',
			'3/Distance/Montana/8']

print('Please enter a password. It must contain both UPPER and lower\
	   case letters, have at least one digit and one special character \
	   [!@#$%^&*_-+=?]. Your password must also be no less than eight [8] \
	   characters long')
password = input()
passTest = 