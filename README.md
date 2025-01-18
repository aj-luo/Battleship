# Battleship Solitaire
Battleship Solitaire Constraint Satisfaction Problem Solver

This is an AI solver of the Battleship Solitaire game, here is a website you can play to understand the game mechanics: https://lukerissacher.com/battleships

Once all the files are downloaded, run the following command in your terminal/cmd prompt: 

python3 battle.py puzzle1.txt output1.txt

battle.py is the code, puzzle1.txt is the puzzle board to be solved, and the result will be stored within output1.txt

puzzle1.txt contains the gameboard, the board is an N x N grid: 

The input file will represent an NxN puzzle and be formatted as follows:

On the first line will be the puzzle’s row constraints written as a string of N numbers (note that row constraints are usually written to the left or the right of each row when viewing examples of these puzzle).
On the second line will be the puzzle’s column constraints written as a string of N numbers (note that column constraints are usually written on top or bottom of each column when viewing examples of these puzzle).
On the third line will be 1-4 numbers, representing the number of submarines, destroyers, cruisers and battleships, in that order. Some of the smaller puzzles are too small to contain larger ships, so if there are less than 4 numbers in this row you can assume that no ships of that size exist in this puzzle.
The remaining lines will represent the starting layout of the puzzle, which indicates any starting values you have to work with. Each line will represent a row of the Battleship Solitaire grid as a string of characters, with each character representing a single square in that row. There are 8 possible characters for this section of the input file:

‘0’ (zero) represents no hint for that square
‘S’ represents a submarine,
‘W’ represents water
‘L’ represents the left end of a horizontal ship,
‘R’ represents the right end of a horizontal ship,
‘T’ represents the top end of a vertical ship, 
‘B’ represents the bottom end of a vertical ship, and
'M' represents a middle segment of a ship (horizontal or vertical).

The output will be similar in format to the input, except only the contents of the final solution to the NxN board will be printed. Each character in the output corresponds to the contents of a cell in the solution. Similar to the input file, there are 7 possible values for each square in the solution grid (there should be no '0' characters left once the puzzle is solved). For example, the correct output for the input example above would be:
