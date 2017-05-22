#! python3
#passLocker, an insecure password storage and retrieval system
# runnig this program through it's batch file extension passes a command line argument [account] to the .py progtam. Effectivly creating a persistant clipboard

Passwords ={'email':'emailpass',
			'blog': 'blogpass',
			'luggage': 'luggagepass'}

import sys, pyperclip
if len(sys.argv) <2:
	print('Usage: python passLocker.py [account] - copy account password')
	sys.exit()

account= sys.argv[1] # first command line argument is that account name

if account in Passwords:
	pyperclip.copy(Passwords[account])
	print('Password for '+account+' copied to clipboard')
else:
	print('There is no account named '+account)
	addto= input('add account? (Y/N): ')
	if addto.lower() == 'y':
		newAccount= input('enter new account: ')
		newPass= input('enter new password: ')
		Passwords.setdefault(str(newAccount),str(newPass))
	else: 
		print('maybe next time')