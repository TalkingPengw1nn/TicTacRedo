import random

# draws grid space
def drawGrid ():
	for row in range(2, -1, -1):
		print("\n+---+---+---+")
		print("|", end = "")
		for col in range(3):
			print("", grid[row][col], end = " |")
	print("\n+---+---+---+")

# checks for win
def checkWin():
	for row in range(3):
		if grid[row][0] == grid[row][1] == grid[row][2] != " ": # checks rows for win
			return True
			
		col = row
		if grid[0][col] == grid[1][col] == grid[2][col] != " ": # checks columns...
			return True
	
	if grid[0][0] == grid[1][1] == grid[2][2] != " ": # checks principle diagonal...
		return True
		
	if grid[0][2] == grid[1][1] == grid[2][0] != " ": # checks anti diagonal...
		return True	
	
	return False

# variables for grid positions
grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# variables for player symbols
player1 = 'X'
player2 = 'O'
playerMarks = [player1, player2]
playerTurn = random.choice(playerMarks) #randomises the first person's mark

turnCount = 0 # variable to count up to draw
emptyBox = 0 # variable to track the empty space for REDO mode
REDO = False # variable to approve REDO mode


print("<Use keypad for input>\n<values from 1 to 9 as positioned in keypad>")
drawGrid();

while True:
	try:
		position = int(input("player's turn: (" + playerTurn + ") --> ")) #takes players input
	
	except ValueError:
		print(">>Invalid input<<")
		continue
	
	if position < 1 or position > 9:
		print(">>Invalid range<<")
		continue
	
	# converts input value into row and column index
	row = int((position - 1) / 3)
	col = int((position - 1) % 3)	
		
	if not REDO:	# Normal MODE...default	
		if grid[row][col] != " ":
			print(">>Not this space<<")
			continue
					
		grid[row][col] = playerTurn
		
		drawGrid();
		turnCount += 1
		emptyBox = position # last position filled is emptied
	else:			# REDO MODE...after draw
		if grid[row][col] != playerTurn:
			print(">>Not this space<<")
			continue
					
		grid[row][col] = " " # empties chosen position
		
		row = int((emptyBox - 1) / 3)
		col = int((emptyBox - 1) % 3)
		grid[row][col] = playerTurn # inputs into the last empty position
		emptyBox = position # tracks the recently emptied position
		drawGrid();
		
	if checkWin():
		print("<<<player" + playerTurn + " wins!>>>")
		break
	elif turnCount == 9:
		print("<<<Draw!>>> \nLet's begin REDO mode.")
		REDO = True
		turnCount = 0 # ensures block code is executed only once
		grid[row][col] = " "
		drawGrid();
	 
	# shifts turn between players
	playerTurn =  player2 if playerTurn == player1 else player1
