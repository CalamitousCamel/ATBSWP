tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(var):
	colwidths= [0] *len(var)
	pad= 2											# sets padding distance between printed columns. Used instead of end=' ' to maintain title justification
	for n in range(len(var)):						# finds and stores longest sting length per list
		for i in var[n]:
			if len(i) > colwidths[n]:
				colwidths[n]=len(i)
		pass
	
	print('\n'+'table'.upper().center(len(var)*pad+sum(colwidths),'=')) # prints title header (centered over the table)
	for x in range(len(var[0])):										# loop prints var[0][0], var[1][0] etc. printing a new line for every iteration back to var[0]
		print()
		for y in range(len(var)):
			print(var[y][x].center(colwidths[y]+pad),end='') # just thought it looked better with center-justified columns
	print()


printTable(tableData)