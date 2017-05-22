'''while True:
		age= input('enter your age: ')
	if age.isdecimal():
		break
	print('please enter a number for your age')

while True:
	password= input('\nenter your password.\nletters and numbers only please: ')
	if password.isalnum():
		break
	print('\n'+r'please do not use any special characters (_-*%!@ etc.)')'''

def printpicnic(itemsDict, leftWidth, rightWidth):
	print('picnic items'.upper().center(leftWidth+rightWidth, '-'))
	for k,v in itemsDict.items():
		print(k.ljust(leftWidth, '-')+str(v).rjust(rightWidth))

picnicitems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies':8000}
printpicnic(picnicitems, 12, 5)
printpicnic(picnicitems, 20, 6)