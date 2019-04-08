import pprint

def BattleshipBoard():
	board_surface={"A":["O","O","O","O","O","O","O","O","O","O"],
					"B":["O","O","O","O","O","O","O","O","O","O"],
					"C":["O","O","O","O","O","O","O","O","O","O"],
					"D":["O","O","O","O","O","O","O","O","O","O"],
					"E":["O","O","O","O","O","O","O","O","O","O"],
					"F":["O","O","O","O","O","O","O","O","O","O"],
					"G":["O","O","O","O","O","O","O","O","O","O"],
					"H":["O","O","O","O","O","O","O","O","O","O"],
					"I":["O","O","O","O","O","O","O","O","O","O"],
					"J":["O","O","O","O","O","O","O","O","O","O"]
					}
	board_subsea={"A":["O","O","O","O","O","O","O","O","O","O"],
					"B":["O","O","O","O","O","O","O","O","O","O"],
					"C":["O","O","O","O","O","O","O","O","O","O"],
					"D":["O","O","O","O","O","O","O","O","O","O"],
					"E":["O","O","O","O","O","O","O","O","O","O"],
					"F":["O","O","O","O","O","O","O","O","O","O"],
					"G":["O","O","O","O","O","O","O","O","O","O"],
					"H":["O","O","O","O","O","O","O","O","O","O"],
					"I":["O","O","O","O","O","O","O","O","O","O"],
					"J":["O","O","O","O","O","O","O","O","O","O"]
					}
	return board_surface, board_subsea


def updateBattleshipBoard(board_subsea, board_surface, coordinate, symbol):
	for element in coordinate:
		if element[2] == 0:
			row = chr(element[0]+65)
			if not board_subsea[row][element[1]] == "*":
				board_subsea[row][element[1]]= symbol
		if element[2] == 1:
			row = chr(element[0]+65)
			if not board_surface[row][element[1]] == "*":
				board_surface[row][element[1]]= symbol
	return board_subsea, board_surface
	
def printBattleshipBoard(board_subsea, board_surface):
	print("The subsea coordinates are shown below:")
	print("       ",1,"  ",2,"  ",3,"  ",4,"  ",5,"  ",6,"  ",7,"  ",8,"  ",9,"  ",10)
	pprint.pprint(board_subsea)
	print(" ")
	print("The surface coordinates are shown below:")
	print("       ",1,"  ",2,"  ",3,"  ",4,"  ",5,"  ",6,"  ",7,"  ",8,"  ",9,"  ",10)
	pprint.pprint(board_surface)

	
if __name__ == '__main__':
	board_surface, board_subsea = BattleshipBoard()
	coordinate = [(6, 1, 0), (6, 2, 0), (6, 3, 0), (6, 4, 0)]
	symbol = "*"
	board_subsea, board_surface = updateBattleshipBoard(board_subsea, board_surface, coordinate, symbol)
	printBattleshipBoard(board_subsea, board_surface)
