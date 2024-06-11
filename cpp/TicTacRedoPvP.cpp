#include <iostream>
//using namespace std;

//draws the grid
void drawGrid(char grid[3][3]) {
    std::cout << "\n" << std::endl;
    std::cout << "[ " << grid[2][0] << " ][ " << grid[2][1] << " ][ " << grid[2][2] << " ]" << std::endl;    
    std::cout << "[ " << grid[1][0] << " ][ " << grid[1][1] << " ][ " << grid[1][2] << " ]" << std::endl;
    std::cout << "[ " << grid[0][0] << " ][ " << grid[0][1] << " ][ " << grid[0][2] << " ]" << std::endl;
    std::cout << "\n" << std::endl;
}

//checks for win
bool checkWin(char grid[3][3]) {
	int row = 0;
    while (row < 3) {
        //checking rows for win
        if (grid[row][0] != ' ' && grid[row][0] == grid[row][1] && grid[row][1] == grid[row][2]) {
            return true;
        }
        //checking columns for win
        int col = row;
        if (grid[0][col] != ' ' && grid[0][col] == grid[1][col] && grid[1][col] == grid[2][col]) {
            return true;
        }
        //checking principle diagonal for win
        if (grid[0][0] != ' ' && grid[0][0] == grid[1][1] && grid[1][1] == grid[2][2]) {
            return true;
        }
        //checking anti-diagonal for win
        if (grid[2][0] != ' ' && grid[2][0] == grid[1][1] && grid[1][1] == grid[0][2]) {
            return true;
        }
        row++;
    }
    return false;
}


int main() {
    //initialize grid elements
    char grid[3][3] = {
        {' ', ' ', ' '},
        {' ', ' ', ' '},
        {' ', ' ', ' '}
    };
    
    //variable for grid positioning
    int position;
    int row, col;
    int emptyBox = 0;
    
    //variable for turn count up to DRAW
    int turnCount = 0;
    
    //variable for mode condition
    bool redoMode = false;
    
    //mark for each player
    const char player1 = 'X';
    const char player2 = 'O';
    
    //randomises the first player mark
    srand(time(nullptr));
    int firstPerson = rand() % 2; //values are 0 or 1
    char playerTurn = (firstPerson == 0)? player1 : player2; //varibale for player's turn and printing 'X' or 'O' mark on grid

	//displays initial grid space
    std::cout << "(Use keypad to select position.)" << std::endl;    
    drawGrid(grid);

    
    while (true) {
		//diplays player's turn
        std::cout << "Player Turn = " << playerTurn << std::endl;
        //takes input from players
        std::cout << "______________________________" << std::endl;
        std::cin >> position;
        std::cout << "______________________________" << std::endl;
        
        //calculates row and column index
		row = (position - 1)/3;
		col = (position - 1)%3;
        
        //assesses if input wihtin range
        if (position > 9 || position < 1) {
            std::cout << "Invalid entry. Retry." << std::endl;
        }
        else if (!redoMode) { //REGULAR mode...
			//assesses if position is available...Normal mode
			if (grid[row][col] != ' ') {
				std::cout << "Position is filled. Retry." << std::endl;
			}
			
			//tracks the last empty space incase of draw...last position is emptied		
			emptyBox = position;
			
            grid[row][col] = playerTurn; //inputs player position
            turnCount++; //counts the number of turns
            
        }
        else {	//REDO mode...
				//assesses if position is available...REDO mode
				if (grid[row][col] != playerTurn) {
					std::cout << "Can't use this position for " << playerTurn << std::endl;
				}
				else 	{
					grid[row][col] = ' ';//empties the values on the picked position
				
					//calculates row and column index for last empty space
					row = (emptyBox - 1)/3;
					col = (emptyBox - 1)%3;
				
					grid[row][col] = playerTurn; //inputs into the last empty position
								
					emptyBox = position; //tracks recently emptied position
			}
		}
		
        //clears error flags (if any) and discards the errorous input values
        std::cin.clear(); //clears error flags
        std::cin.ignore(1000, '\n'); //skiping to the next new line \n (already present in input) up to 10000 char
		
		drawGrid(grid); //displays grid in play
		
        //checks for win or draw
        if (checkWin(grid)) {
			std::cout << "==============================" << std::endl;
            std::cout << "Player" << playerTurn << "WINS!!!" << std::endl; 
            std::cout << "==============================" << std::endl;
            break;
        }
        else if (turnCount == 9) {
			std::cout << "==============================" << std::endl;
            std::cout << "DRAW!\n" << std::endl;
            std::cout << "Now begins the REDO mode.\n(You exchange your mark with last empty place)" << std::endl;
            turnCount = 0;
            redoMode = true;
            grid[row][col] = ' '; //REDO case...empties the picked position
            drawGrid(grid); //displays grid with one empty space
        }
        
        playerTurn = (playerTurn == player2)? player1 : player2; //Alternates the player turn
        
    }
    
    std::cout << "\nEND." << std::endl;
    return 0;
}
