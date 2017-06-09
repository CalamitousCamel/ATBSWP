#! Python3
# Prompts user for password and tests it for strength before exiting
import re
from getpass import getpass

def passCheck():
	upperCheck = re.compile(r'[A-Z]')
	lowerCheck = re.compile(r'[a-z]')
	digitCheck = re.compile(r'[0-9]')
	charCheck = re.compile(r'[\!\@\#\$\%\^\&\*\_\-\+\=\?]')
	while True:
		password = getpass(prompt='\nPlease enter a password: ')
		if len(password) < 8:
			print('Please include at least than 8 characters')
		if lowerCheck.search(password) is None:
			print('Please include at least one lowercase letter [a-z]')
		if upperCheck.search(password) is None:
			print('Please include at least one uppercase letter [A-Z]')
		if digitCheck.search(password) is None:
			print('Please include at least one digit [0-9] ')
		if charCheck.search(password) is None:
			print('Please include at least one special character '
				  '[!@#$%^&*_-+=?]')
			
		if len(password) > 7:
			if lowerCheck.search(password):
				if upperCheck.search(password):
					if digitCheck.search(password):
						if charCheck.search(password):
							print('Password accepted')
							break


print('Please enter a password. It must contain both UPPERCASE and '
	  'lowercase letters, have at least one digit and one special '
	  'character [!@#$%^&*_-+=?]. Your password must also be no less '
	  'than eight [8] characters long')
passCheck()

'''
testPasslist= ([r'9!Products!Taken!2',
			'8%Broke%Neighbor%6',
			'8:Members:Southern:9',
			'8&Planet&Home&7',
			'0;Industry;Wheels;2',
			'1@Inch@Plane@6',
			'4?Chance?Science?9',
			'4_Spent_Round_4',
			'5/August/Head/2',
			'3/Distance/Montana/8'])
'''