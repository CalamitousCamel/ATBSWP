theboard= {'tr':' ', 'tc':' ', 'tl':' ', 'mr':' ', 'mc':' ', 'ml':' ', 'br':' ', 'bc':' ', 'bl':' '}

def printboard(board):
    print(board['tl'] + ' | ' + board['tc'] + '|' + board['tr'])
    print('--+--+--')
    print(board['ml'] + ' | ' + board['mc'] + '|' + board['mr'])
    print('--+--+--')
    print(board['bl'] + ' | ' + board['bc'] + '|' + board['br'])

printboard(theboard)
player="X"
for _ in range(9):
	print("It's "+player+"'s turn.")
	move=input("Move on which space?: ")
	theboard[move]= player
	if player == "X":
		player = "O"
	else: 
		player= "X"
	printboard(theboard)