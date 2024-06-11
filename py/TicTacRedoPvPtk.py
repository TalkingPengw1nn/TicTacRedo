from tkinter import *
import random

def game(_row, _col):
	global playerTurn
	global turnCount
	global REDO
	global emptyBox
	global emptyCount
	
	#Normal mode...
	if buttons[_row][_col]['text'] == "" and not checkWin() and not REDO:
		buttons[_row][_col]['text'] = playerTurn
		playerTurn =  player2 if playerTurn == player1 else player1
		turnShow.config(text = "player turn: (" + playerTurn + ")")
		turnCount += 1
		
	#REDO mode...
	if buttons[_row][_col]['text'] == playerTurn and not checkWin() and REDO:
		buttons[int((emptyBox-1)/3)][int((emptyBox-1)%3)].config(text = playerTurn, bg = 'tomato', fg = 'black')
		buttons[_row][_col].config(text = "", bg = 'white', fg = 'white')
		emptyBox = 3 * _row + _col + 1
		playerTurn =  player2 if playerTurn == player1 else player1
		turnShow.config(text = "REDO => player turn: (" + playerTurn + ")", fg = 'black')
		turnCount = 0
			
		
	if checkWin():
		turnShow.config(text = "Player (" + playerTurn + ") Wins", fg = 'green')
		
	#case of DRAW...	
	if turnCount == 9:
		turnShow.config(text = "D-R-A-W", fg = 'Blue')
		
		for row in range(3):
			for col in range(3):
				buttons[row][col].config(bg='blue', fg = 'white')
		if emptyCount < 1:
			emptyBox = (3 * _row + _col + 1) 
			emptyCount += 1
		
		#creates a REDO Button for redoMode
		redoButton.config(text="REDO", font = ('fixedsys', 20), width = 8, height = 1,bg = 'tomato',
										command = lambda row = _row, col = _col : redoMode(row, col))
		redoButton.grid(row = 3, column = 2, pady = 5)

#checks for winning position	
def checkWin():
	for row in range(3):
		if buttons[row][0]['text'] != "" and buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text']:
			buttons[row][0].config(bg="green")
			buttons[row][1].config(bg="green")
			buttons[row][2].config(bg="green")
			return True
			
		col = row
		if buttons[0][col]['text'] != "" and buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text']:
			buttons[0][col].config(bg="green")
			buttons[1][col].config(bg="green")
			buttons[2][col].config(bg="green")
			return True
	
	if buttons[0][0]['text'] != "" and buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text']:
		buttons[0][0].config(bg="green")
		buttons[1][1].config(bg="green")
		buttons[2][2].config(bg="green")
		return True
		
	if buttons[2][0]['text'] != "" and buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text']:
		buttons[2][0].config(bg="green")
		buttons[1][1].config(bg="green")
		buttons[0][2].config(bg="green")
		return True	
	
	return False

#cleans the Buttons for restart
def newStart():
	global turnCount
	global REDO	
	global playerTurn
	
	turnCount = 0
	playerTurn = random.choice(playerMarks)
	REDO = False
	
	for row in range(3):
		for col in range(3):
			buttons[row][col].config(text = "", bg = 'grey', fg = 'black')
	
	turnShow.config(text = "player turn: (" + playerTurn + ")", fg = 'black')
	
	redoButton.grid_remove()

#sets the initial Button state for redoMode	
def redoMode(_row, _col):
	global turnCount
	global REDO	
	global emptyBox	
	global playerTurn

	turnCount = 0
	REDO = True
	
	for row in range(3):
		for col in range(3):
			buttons[row][col].config(bg = 'tomato', fg = 'black')
			
	buttons[int((emptyBox-1)/3)][int((emptyBox-1)%3)].config(text = "", bg = 'white', fg = 'white')
			
	
	turnShow.config(text = "REDO => player turn: (" + playerTurn + ")", fg = 'black')
	
	redoButton.grid_remove()
	
	pass
	


window = Tk()
window.title("Tic-Tac-Redo")


buttons = [	['', '', ''],
			['', '', ''],
			['', '', ''] ]

player1 = 'X'
player2 = 'O'
playerMarks = [player1, player2]
playerTurn = random.choice(playerMarks) #randomises the first person's mark
turnCount = 0
emptyCount = 0
emptyBox = 0
REDO = False

#displays playerTurn at top of window
turnShow = Label(window,text = "player turn: (" + playerTurn + ")", font = ('fixedsys', 20))
turnShow.pack(side = "top", pady = 10)

#creates a frame for display
display = Frame(window)
display.pack()

#restarts the game to initial state
restartButton = Button(display, text="Restart", font = ('fixedsys', 20), width = 8, height = 1,bg = 'slate blue',
										command = newStart)
restartButton.grid(row = 3, column = 1, pady = 5)

#declares a REDO button
redoButton = Button(display)

#creates Buttons on the frame, display.
for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(display, text="", font = ('fixedsys', 50), width = 5, height = 2,bg = 'grey',
										command = lambda _row=row, _col=col : game(_row,_col))
        buttons[row][col].grid(row=row,column=col)


mainloop()
