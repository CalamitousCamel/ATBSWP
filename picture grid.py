''' desired output (grid rotated 90 degrees)
	..OO.OO.. 
	.OOOOOOO. 
	.OOOOOOO. 
	..OOOOO.. 
	...OOO... 
	....O....  
'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def printloop(var):
	x,y=0,0
	while x < len(grid[0]):
		print(grid[y][x],end='')
		y+=1
		if y == len(grid):
			x+=1
			y=0
			print()

def floop(var):
	for x in range(len(var[0])):	# prints newline after the nested loop and iterates x+=1. Runs once for every value in var's first list value
		for y in range(len(var)):	# prints the x value in every list, then exits to initial loop for newline. Runs once for every list in var* values in var's first list
			print(var[y][x],end='')
		print()
floop(grid)