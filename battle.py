import sys 
import datetime
 
class Ship:
    def __init__(self, name, type, size):
       '''Initialize a variable'''
       self.name = name
       self.type = type
       self.domain = []
       self.size = size
  
    def prune(self, item):
       self.domain.remove(item)
  
    def get_domain(self):
       return self.domain
  
    def domain_size(self):
       return len(self.domain)
    
    def get_ship_type(self):
        return self.type
    
    def get_ship_name(self):
        return self.name
    
    def add_to_domain(self, value):
        self.domain.append(value)
    
    def get_size(self):
        return self.size


class Puzzle:
    def __init__(self, current):
        self.current = current
    
    def get_current(self):
        return self.current
 
if len(sys.argv) == 3:   
    input_file = sys.argv[1] #the file containing the puzzle   
    output_file = sys.argv[2] #the file the solution 
      
    file = open(input_file, 'r')   
    f = file.readlines()   
      
    modified = []   
    for line in f: #line will be an array of strings, each string represents a row in puzzle   
        if line[-1] == '\n':   
           modified.append(line[:-1])   
        else:   
            modified.append(line)   
  
   #These things are the constraints that we need for puzzle (vertical, horizontal constraints as well as number of pieces)
    row_constraints = {}
    column_constraints = {}

    vertical_constraint = modified[0]
    horizontal_constraint = modified[1]
    
    current = 1
    for i in vertical_constraint:
        if current not in row_constraints:
            row_constraints[current] = int(i)
        current += 1
    current2 = 1
    for i in horizontal_constraint:
        if current2 not in column_constraints:
            column_constraints[current2] = int(i)
        current2 += 1
  
   #the number of each ship that we have
    num_battleship = 0
    num_cruiser = 0
    num_destroyer = 0
    num_submarine = 0
 
    pieces = modified[2]
    if len(pieces) == 4:
        num_battleship = int(pieces[3])
        num_cruiser = int(pieces[2])
        num_destroyer = int(pieces[1])
        num_submarine = int(pieces[0])
    if len(pieces) == 3:
        num_cruiser = int(pieces[2])
        num_destroyer = int(pieces[1])
        num_submarine = int(pieces[0])
    if len(pieces) == 2:
        num_destroyer = int(pieces[1])
        num_submarine = int(pieces[0])
    if len(pieces) == 1:
        num_submarine = int(pieces[0])
 
    #pop off the first 3 lines of the input so we just have the puzzle left
    puzzle = modified[3:]
  
    #we will make our variables and put them all inside a list
    length_of_puzzle = len(puzzle)
 
    puzzle_matrix = {} #this is the starting state of our puzzle 
    for i in range(length_of_puzzle):   
        for j in range(length_of_puzzle):   
            current = puzzle[i][j]  
            position_matrix = (i + 1, j + 1)   
            if position_matrix not in puzzle_matrix:   
                puzzle_matrix[position_matrix] = current
    
    board = Puzzle(puzzle_matrix)
    current_board = board.get_current()

    for coordinate in current_board:
        if current_board[coordinate] == 'S':
            num_submarine -= 1

    row_pieces = {}
    column_pieces = {}
    #get the number of ship pieces in every row and column
    for coordinate in current_board:
        if coordinate[0] not in row_pieces:
            if current_board[coordinate] != 'W' and current_board[coordinate] != '0':
                row_pieces[coordinate[0]] = 1
            else:
                row_pieces[coordinate[0]] = 0
        else:
            if current_board[coordinate] != 'W' and current_board[coordinate] != '0':
                row_pieces[coordinate[0]] += 1
        if coordinate[1] not in column_pieces:
            if current_board[coordinate] != 'W' and current_board[coordinate] != '0':
                column_pieces[coordinate[1]] = 1
            else:
                column_pieces[coordinate[1]] = 0
        else:
            if current_board[coordinate] != 'W' and current_board[coordinate] != '0':
                column_pieces[coordinate[1]] += 1
  
    #do preprocessing, for example, if S is there, surround it with water, if R is there, then its left value must be a M, etc.
    for coordinates in current_board:
        top = coordinates[0] - 1
        bottom = coordinates[0] + 1
        middle_row = coordinates[0]
        left = coordinates[1] - 1
        right = coordinates[1] + 1
        middle_col = coordinates[1]
        if current_board[coordinates] == 'S':
            if (top, left) in current_board:
                current_board[(top, left)] = 'W'
            if (top, middle_col) in current_board:
                current_board[(top, middle_col)] = 'W'
            if (top, right) in current_board:
                current_board[(top, right)] = 'W'
            if (middle_row, left) in current_board:
                current_board[(middle_row, left)] = 'W'
            if (middle_row, right) in current_board:
                current_board[(middle_row, right)] = 'W'
            if (bottom, left) in current_board:
                current_board[(bottom, left)] = 'W'
            if (bottom, middle_col) in current_board:
                current_board[(bottom, middle_col)] = 'W'
            if (bottom, right) in current_board:
                current_board[(bottom, right)] = 'W'
        if current_board[coordinates] == 'B':
            if (top - 1, left) in current_board:
                current_board[(top - 1, left)] = 'W'
            if (top - 1, right) in current_board:
                current_board[(top - 1, right)] = 'W'
            if (top, left) in current_board:
                current_board[(top, left)] = 'W'
            if (top, right) in current_board:
                current_board[(top, right)] = 'W'
            if (middle_row, left) in current_board:
                current_board[(middle_row, left)] = 'W'
            if (middle_row, right) in current_board:
                current_board[(middle_row, right)] = 'W'
            if (bottom, left) in current_board:
                current_board[(bottom, left)] = 'W'
            if (bottom, middle_col) in current_board:
                current_board[(bottom, middle_col)] = 'W'
            if (bottom, right) in current_board:
                current_board[(bottom, right)] = 'W'
        if current_board[coordinates] == 'T':
            if (top, left) in current_board:
                current_board[(top, left)] = 'W'
            if (top, middle_col) in current_board:
                current_board[(top, middle_col)] = 'W'
            if (top, right) in current_board:
                current_board[(top, right)] = 'W'
            if (middle_row, left) in current_board:
                current_board[(middle_row, left)] = 'W'
            if (middle_row, right) in current_board:
                current_board[(middle_row, right)] = 'W'
            if (bottom, left) in current_board:
                current_board[(bottom, left)] = 'W'
            if (bottom, right) in current_board:
                current_board[(bottom, right)] = 'W'
            if (bottom + 1, left) in current_board:
                current_board[(bottom + 1, left)] = 'W'
            if (bottom + 1, right) in current_board:
                current_board[(bottom + 1, right)] = 'W'
        if current_board[coordinates] == 'L':
            if (top, left) in current_board:
                current_board[(top, left)] = 'W'
            if (middle_row, left) in current_board:
                current_board[(middle_row, left)] = 'W'
            if (bottom, left) in current_board:
                current_board[(bottom, left)] = 'W'
            if (top, middle_col) in current_board:
                current_board[(top, middle_col)] = 'W'
            if (bottom, middle_col) in current_board:
                current_board[(bottom, middle_col)] = 'W'
            if (top, right) in current_board:
                current_board[(top, right)] = 'W'
            if (bottom, right) in current_board:
                current_board[(bottom, right)] = 'W'
            if (top, right + 1) in current_board:
                current_board[(top, right + 1)] = 'W'
            if (bottom, right + 1) in current_board:
                current_board[(bottom, right + 1)] = 'W'
        if current_board[coordinates] == 'R':
            if (top, right) in current_board:
                current_board[(top, right)] = 'W'
            if (middle_row, right) in current_board:
                current_board[(middle_row, right)] = 'W'
            if (bottom, right) in current_board:
                current_board[(bottom, right)] = 'W'
            if (top, middle_col) in current_board:
                current_board[(top, middle_col)] = 'W'
            if (bottom, middle_col) in current_board:
                current_board[(bottom, middle_col)] = 'W'
            if (top, left) in current_board:
                current_board[(top, left)] = 'W'
            if (bottom, left) in current_board:
                current_board[(bottom, left)] = 'W'
            if (bottom, left - 1) in current_board:
                current_board[(bottom, left - 1)] = 'W'
            if (top, left - 1) in current_board:
                current_board[(top, left - 1)] = 'W'
    
    #preprocess to wipe out any rows or columns which already satisfy the piece constraint
    rows_to_clear = []
    columns_to_clear = []
    for i in row_pieces:
        if row_constraints[i] == row_pieces[i]:
            rows_to_clear.append(i)
    for i in column_pieces:
        if column_constraints[i] == column_pieces[i]:
            columns_to_clear.append(i)
    for coordinate in current_board:
        if coordinate[0] in rows_to_clear or coordinate[1] in columns_to_clear:
            if current_board[coordinate] == '0':
                current_board[coordinate] = 'W'
    
    #we need to start populating the domains of the variables aka our ships
    ship_list = [] #this contains all our variables/ship
    for i in range(num_battleship):
        battleship_name = "battleship" + str(i + 1)
        battleship = Ship(battleship_name, "battleship", 4)
        ship_list.append(battleship)
    for i in range(num_cruiser):
        cruiser_name = "cruiser" + str(i + 1)
        cruiser = Ship(cruiser_name, "cruiser", 3)
        ship_list.append(cruiser)
    for i in range(num_destroyer):
        destroyer_name = "destroyer" + str(i + 1)
        destroyer = Ship(destroyer_name, "destroyer", 2)
        ship_list.append(destroyer)
    for i in range(num_submarine):
        submarine_name = "submarine" + str(i + 1)
        sub = Ship(submarine_name, "submarine", 1)
        ship_list.append(sub)
    
    current_board = board.get_current()
    for ship in ship_list:
        ship_type = ship.get_ship_type()

        if ship_type == "submarine":
            for coordinates in current_board:
                if current_board[coordinates] == '0':
                    ship.add_to_domain((coordinates, coordinates))

        if ship_type == "destroyer":
            for coordinates in current_board:
                if current_board[coordinates] == '0' or current_board[coordinates] == 'L' or current_board[coordinates] == 'T':
                    if current_board[coordinates] == '0' or current_board[coordinates] == 'L':
                        if (coordinates[0], coordinates[1] + 1) in current_board and (current_board[(coordinates[0], coordinates[1] + 1)] == '0' or current_board[(coordinates[0], coordinates[1] + 1)] == 'R'):
                            ship.add_to_domain((coordinates, (coordinates[0], coordinates[1] + 1)))
                    if current_board[coordinates] == '0' or current_board[coordinates] == 'T':
                        if (coordinates[0] + 1, coordinates[1]) in current_board and (current_board[(coordinates[0] + 1, coordinates[1])] == '0' or current_board[(coordinates[0] + 1, coordinates[1])] == 'B'):
                            ship.add_to_domain((coordinates, (coordinates[0] + 1, coordinates[1])))

        if ship_type == "cruiser":
            for coordinates in current_board:
                if current_board[coordinates] == '0' or current_board[coordinates] == 'L' or current_board[coordinates] == 'T':  
                    coordinate1 = (coordinates[0], coordinates[1] + 2)
                    coordinate2 = (coordinates[0], coordinates[1] + 1)
                    coordinate3 = (coordinates[0] + 2, coordinates[1])
                    coordinate4 = (coordinates[0] + 1, coordinates[1])
                    if current_board[coordinates] == '0' or current_board[coordinates] == 'L':
                        if coordinate1 in current_board and (current_board[coordinate2] == '0' or current_board[coordinate2] == 'M') and (current_board[coordinate1] == '0' or current_board[coordinate1] == 'R'):
                            ship.add_to_domain((coordinates, (coordinates[0], coordinates[1] + 2)))
                    if current_board[coordinates] == '0' or current_board[coordinates] == 'T':
                        if coordinate3 in current_board and (current_board[coordinate4] == '0' or current_board[coordinate4] == 'M') and (current_board[coordinate3] == '0' or current_board[coordinate3] == 'B'):
                            ship.add_to_domain((coordinates, (coordinates[0] + 2, coordinates[1])))
        if ship_type == "battleship":
            for coordinates in current_board:
                if current_board[coordinates] == '0' or current_board[coordinates] == 'L' or current_board[coordinates] == 'T':
                    #list of bools
                    if (coordinates[0], coordinates[1] + 3) in current_board:
                        intermediate_right_permissible1 = (current_board[(coordinates[0], coordinates[1] + 1)] == '0' or current_board[(coordinates[0], coordinates[1] + 1)] == 'M')
                        intermediate_right_permissible2 = (current_board[(coordinates[0], coordinates[1] + 2)] == '0' or current_board[(coordinates[0], coordinates[1] + 2)] == 'M')
                        right_three_away_value = (current_board[(coordinates[0], coordinates[1] + 3)] == '0' or current_board[(coordinates[0], coordinates[1] + 3)] == 'R')
                        if current_board[coordinates] == '0' or current_board[coordinates] == 'L':
                            if intermediate_right_permissible1 and intermediate_right_permissible2 and right_three_away_value:
                                ship.add_to_domain((coordinates, (coordinates[0], coordinates[1] + 3)))
                            
                    if (coordinates[0] + 3, coordinates[1]) in current_board:
                        intermediate_bottom_permissible1 = (current_board[(coordinates[0] + 1, coordinates[1])] == '0' or current_board[(coordinates[0] + 1, coordinates[1])] == 'M')
                        intermediate_bottom_permissible2 = (current_board[(coordinates[0] + 2, coordinates[1])] == '0' or current_board[(coordinates[0] + 2, coordinates[1])] == 'M')
                        bottom_three_away_value = (current_board[(coordinates[0] + 3, coordinates[1])] == '0' or current_board[(coordinates[0] + 3, coordinates[1])] == 'B')
                        if current_board[coordinates] == '0' or current_board[coordinates] == 'T':
                            if intermediate_bottom_permissible1 and intermediate_bottom_permissible2 and bottom_three_away_value:
                                ship.add_to_domain((coordinates, (coordinates[0] + 3, coordinates[1])))
    

    #need to define the constraints

    def row_constraint(board):
        row_constraint = row_constraints
        row_values = {}
        for i in range(length_of_puzzle):
            row_values[i + 1] = 0
        for coordinate in board:
            if board[coordinate] != '0' and board[coordinate] != 'W':
                row_values[coordinate[0]] += 1
        for row in row_values:
            if (row_values[row] > row_constraint[row]):
                return False
        return True
    
    def column_constraint(board):
        column_constraint = column_constraints
        column_values = {}
        for i in range(length_of_puzzle):
            column_values[i + 1] = 0
        for coordinate in board:
            if board[coordinate] != '0' and board[coordinate] != 'W':
                column_values[coordinate[1]] += 1
        for column in column_values:
            if (column_values[column] > column_constraint[column]):
                return False
        return True
    
    #we call this if the piece is a submarine or a horizontal piece
    def distance_constraint_horizontal(board, start, end):
        #if its a horizontal piece
        hstart_top = (start[0] - 1, start[1])
        hstart_top_left = (start[0] - 1, start[1] - 1)
        hstart_top_right = (start[0] - 1, start[1] + 1)
        hstart_middle_left = (start[0], start[1] - 1)
        hstart_middle_right = (start[0], start[1] + 1)
        hstart_bottom = (start[0] + 1, start[1])
        hstart_bottom_left = (start[0] + 1, start[1] - 1)
        hstart_bottom_right = (start[0] + 1, start[1] + 1)

        hend_top = (end[0] - 1, end[1])
        hend_top_right = (end[0] - 1, end[1] + 1)
        hend_middle_right = (end[0], end[1] + 1)
        hend_bottom = (end[0] + 1, end[1])
        hend_bottom_right = (end[0] + 1, end[1] + 1)
        if start[0] == end[0]:
            if start == end: #this is a submarine
                if board[start] != '0':
                    return False
                if hstart_top in board:
                    if board[hstart_top] != '0' and board[hstart_top] != 'W':
                        return False
                if hstart_top_left in board:
                    if board[hstart_top_left] != '0' and board[hstart_top_left] != 'W':
                        return False
                if hstart_top_right in board:
                    if board[hstart_top_right] != '0' and board[hstart_top_right] != 'W':
                        return False
                if hstart_middle_left in board:
                    if board[hstart_middle_left] != '0' and board[hstart_middle_left] != 'W':
                        return False
                if hstart_middle_right in board:
                    if board[hstart_middle_right] != '0' and board[hstart_middle_right] != 'W':
                        return False
                if hstart_bottom in board:
                    if board[hstart_bottom] != '0' and board[hstart_bottom] != 'W':
                        return False
                if hstart_bottom_left in board:
                    if board[hstart_bottom_left] != '0' and board[hstart_bottom_left] != 'W':
                        return False
                if hstart_bottom_right in board:
                    if board[hstart_bottom_right] != '0' and board[hstart_bottom_right] != 'W':
                        return False
                return True
            else:  #this is not a submarine, its a normal horizontal piece
                if end[1] - start[1] >= 1: #this is either a destroyer cruiser or battleship
                    if board[start] != '0' and board[start] != 'L':
                        return False
                    if board[end] != '0' and board[end] != 'R':
                        return False
                    if hstart_top in board:
                        if board[hstart_top] != '0' and board[hstart_top] != 'W':
                            return False
                    if hstart_top_left in board:
                        if board[hstart_top_left] != '0' and board[hstart_top_left] != 'W':
                            return False
                    if hstart_middle_left in board:
                        if board[hstart_middle_left] != '0' and board[hstart_middle_left] != 'W':
                            return False
                    if hstart_bottom_left in board:
                        if board[hstart_bottom_left] != '0' and board[hstart_bottom_left] != 'W':
                            return False
                    if hstart_bottom in board:
                        if board[hstart_bottom] != '0' and board[hstart_bottom] != 'W':
                            return False
                    if hend_top in board:
                        if board[hend_top] != '0' and board[hend_top] != 'W':
                            return False
                    if hend_top_right in board:
                        if board[hend_top_right] != '0' and board[hend_top_right] != 'W':
                            return False
                    if hend_middle_right in board:
                        if board[hend_middle_right] != '0' and board[hend_middle_right] != 'W':
                            return False
                    if hend_bottom_right in board:
                        if board[hend_bottom_right] != '0' and board[hend_bottom_right] != 'W':
                            return False
                    if hend_bottom in board:
                        if board[hend_bottom] != '0' and board[hend_bottom] != 'W':
                            return False
                    total_useless = 0
                    if board[start] == '0':
                        total_useless += 1
                    if board[end] == '0':
                        total_useless += 1
                    row_number = start[0]
                    column_number = start[1] + 1
                    while column_number != end[1]: #while the column isnt the end column
                        current = board[(row_number, column_number)]
                        if current == '0':
                            total_useless += 1
                        if current != '0' and current != 'M':
                            return False
                        if (row_number - 1, column_number) in board:
                            if board[(row_number - 1, column_number)] != '0' and board[(row_number - 1, column_number)] != 'W':
                                return False
                        if (row_number + 1, column_number) in board:
                            if board[(row_number + 1, column_number)] != '0' and board[(row_number + 1, column_number)] != 'W':
                                return False
                        column_number += 1

                    if total_useless == 0: #this means the area is already occupied by another ship of same type
                        return False     

                    return True
    
    #we call this function if piece is a vertical piece
    def distance_constraint_vertical(board, start, end):
        hstart_top = (start[0] - 1, start[1])
        hstart_top_left = (start[0] - 1, start[1] - 1)
        hstart_top_right = (start[0] - 1, start[1] + 1)
        hstart_middle_left = (start[0], start[1] - 1)
        hstart_middle_right = (start[0], start[1] + 1)

        hend_middle_left = (end[0], end[1] - 1)
        hend_middle_right = (end[0], end[1] + 1)
        hend_bottom = (end[0] + 1, end[1])
        hend_bottom_left = (end[0] + 1, end[1] - 1)
        hend_bottom_right = (end[0] + 1, end[1] + 1)

        if end[0] - start[0] >= 1: #this is either a destroyer cruiser or battleship
                    if board[start] != '0' and board[start] != 'T':
                        return False
                    if board[end] != '0' and board[end] != 'B':
                        return False
                    

                    if hstart_top in board:
                        if board[hstart_top] != '0' and board[hstart_top] != 'W':
                            return False
                    if hstart_top_left in board:
                        if board[hstart_top_left] != '0' and board[hstart_top_left] != 'W':
                            return False
                    if hstart_top_right in board:
                        if board[hstart_top_right] != '0' and board[hstart_top_right] != 'W':
                            return False
                    if hstart_middle_left in board:
                        if board[hstart_middle_left] != '0' and board[hstart_middle_left] != 'W':
                            return False
                    if hstart_middle_right in board:
                        if board[hstart_middle_right] != '0' and board[hstart_middle_right] != 'W':
                            return False
                    if hend_middle_right in board:
                        if board[hend_middle_right] != '0' and board[hend_middle_right] != 'W':
                            return False
                    if hend_middle_left  in board:
                        if board[hend_middle_left] != '0' and board[hend_middle_left] != 'W':
                            return False
                    if hend_bottom_right in board:
                        if board[hend_bottom_right] != '0' and board[hend_bottom_right] != 'W':
                            return False
                    if hend_bottom in board:
                        if board[hend_bottom] != '0' and board[hend_bottom] != 'W':
                            return False
                    if hend_bottom_left in board:
                        if board[hend_bottom_left] != '0' and board[hend_bottom_left] != 'W':
                            return False
                    
                    total_useless = 0
                    if board[start] == '0':
                        total_useless += 1
                    if board[end] == '0':
                        total_useless += 1

                    row_number = start[0] + 1
                    column_number = start[1]
                    while row_number != end[0]: #while the row isnt the end row
                        current = board[(row_number, column_number)]
                        if current == '0':
                            total_useless += 1
                        if current != '0' and current != 'M':
                            return False
                        if (row_number, column_number - 1) in board:
                            if board[(row_number, column_number - 1)] != '0' and board[(row_number, column_number - 1)] != 'W':
                                return False
                        if (row_number, column_number + 1) in board:
                            if board[(row_number, column_number + 1)] != '0' and board[(row_number, column_number + 1)] != 'W':
                                return False
                        row_number += 1
                    
                    if total_useless == 0: #this means the area is already occupied by another ship of same type
                        return False   

                    return True
    
    def add_to_board(board, start, end):
        if start == end: #this is a submarine
            board[start] = 'S'
        elif start[0] == end[0] and start != end: #this is a horizontal piece
            board[start] = 'L'
            board[end] = 'R'
            current_row = start[0]
            current_column = start[1] + 1
            while current_column != end[1]:
                board[(current_row, current_column)] = 'M'
                current_column += 1
        elif start[0] < end[0]: #this is a vertical piece
            board[start] = 'T'
            board[end] = 'B'
            current_row = start[0] + 1
            current_column = start[1]
            while current_row != end[0]:
                board[(current_row, current_column)] = 'M'
                current_row += 1

    #this will be the backtracker
    def backtrack(board, current_ship):
        #base case, we are at the last ship
        if current_ship == len(ship_list) - 1:
            ship = ship_list[current_ship] #this is the ship we are currently iterating
            length_domain = ship.domain_size()
            for coordinates in ship.get_domain():
                trues = 0
                if coordinates[0][0] == coordinates[1][0]: #this is a horizontal piece or submarine
                    if distance_constraint_horizontal(board, coordinates[0], coordinates[1]):
                        trues += 1
                if coordinates[0][0] < coordinates[1][0]: #this is a vertical piece
                    if distance_constraint_vertical(board, coordinates[0], coordinates[1]):
                        trues += 1
                copy_of_board = board.copy() #make a copy to edit, this is our current new board
                add_to_board(copy_of_board, coordinates[0], coordinates[1])
                if column_constraint(copy_of_board):
                    trues += 1
                if row_constraint(copy_of_board):
                    trues += 1

                if trues == 3:
                    return (True, copy_of_board)
            return (False, 0)

        else: #not in base case
            ship = ship_list[current_ship] #this is the ship we are currently iterating
            length_domain = ship.domain_size()
            ship_domain = ship.get_domain()
            for coordinates in ship_domain:
                trues = 0
                if coordinates[0][0] == coordinates[1][0]: #this is a horizontal piece or submarine
                    if distance_constraint_horizontal(board, coordinates[0], coordinates[1]):
                        trues += 1
                if coordinates[0][0] < coordinates[1][0]: #this is a vertical piece
                    if distance_constraint_vertical(board, coordinates[0], coordinates[1]):
                        trues += 1
                copy_of_board = board.copy() #make a copy to edit, this is our current new board
                add_to_board(copy_of_board, coordinates[0], coordinates[1])
                if column_constraint(copy_of_board):
                    trues += 1
                if row_constraint(copy_of_board):
                    trues += 1
                if trues == 3: #if trues equals 3, that means the constraints are satistied for this domain value/coordinate
                    satisfy = backtrack(copy_of_board, current_ship + 1)
                    if satisfy[0]: #if what we get from the recursion (the tuple) is true, then we simply return it
                        return satisfy
            return (False, 0)

    result = backtrack(board.get_current(), 0)
    
    solution_board = result[1]
    for coordinate in solution_board:
        if solution_board[coordinate] == '0':
            solution_board[coordinate] = 'W'
    
    def convert_to_string(puzzle):  
        final_string = ""  
        current = 0 
        for i in puzzle:  
            if current != 0 and current % length_of_puzzle == 0:  
                final_string += "\n"  
            number = puzzle[i]  
            final_string += str(number)  
            current += 1  
        final_string += "\n"  
        return final_string  
    
    output_thing = open(output_file, "w")  

    output_thing = open(output_file, "w")  
    output_thing.write(convert_to_string(solution_board)) 






    

