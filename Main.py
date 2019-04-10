import pprint
import Login
import Create_Account
import Userships
import Computerships
import Print_Battleship_Board
import Attack

#Main Program
print("Welcome to Battleships!")
print("1: Login")
print("2: Create account")
selection_str = input("Enter selection: ")

#Promote user to select Login or Create account.
while True:
	try:
		selection  = int(selection_str)
		if selection == 1:
			Login.Login()
			break
		elif selection == 2:
			Create_Account.CreateAccount()
			break
		else:
			selection_str = input("Please choose 1 or 2.\nEnter selection: ")
	except ValueError:
		selection_str = input("Please choose 1 or 2.\nEnter selection:")

input("Press enter to begin.\n\n")

#Show the battleship board.
board_surface, board_subsea = Print_Battleship_Board.BattleshipBoard()
print("			Battleship Board		\n")	
print("The surface coordinates are shown below:")
print("       ",1,"  ",2,"  ",3,"  ",4,"  ",5,"  ",6,"  ",7,"  ",8,"  ",9,"  ",10)
pprint.pprint(board_surface)
print(" ")
print("The subsea coordinates are shown below:")
print("       ",1,"  ",2,"  ",3,"  ",4,"  ",5,"  ",6,"  ",7,"  ",8,"  ",9,"  ",10)

pprint.pprint(board_subsea)
print("\n")

#Ask for userships
user_submarine, user_carrier = Userships.Userships()
user_ship = user_submarine + user_carrier
board_subsea, board_surface = Print_Battleship_Board.updateBattleshipBoard(board_subsea, board_surface, user_submarine, "S")
board_subsea, board_surface = Print_Battleship_Board.updateBattleshipBoard(board_subsea, board_surface, user_carrier, "C")
Print_Battleship_Board.printBattleshipBoard(board_subsea, board_surface)


#Generate computerships
computer_submarine, computer_carrier = Computerships.Computerships()
#Bprint(computer_submarine, computer_carrier)

#Start the battle.
input("Press enter to start the battle!\n")
board_surface, board_subsea = Print_Battleship_Board.BattleshipBoard() 				#Initiate the battleboard.
while True:
	#User Attack
	for attack in Attack.AttackArea(Attack.UserAttack()):
		if attack in computer_submarine:
			board_subsea, board_surface = Print_Battleship_Board.updateBattleshipBoard(board_subsea, board_surface, [attack], "*")
			computer_submarine.remove(attack)
		elif attack in computer_carrier:
			board_subsea, board_surface = Print_Battleship_Board.updateBattleshipBoard(board_subsea, board_surface, [attack], "*")
			computer_carrier.remove(attack)
		else: 
			board_subsea, board_surface = Print_Battleship_Board.updateBattleshipBoard(board_subsea, board_surface, [attack], "X")
	Print_Battleship_Board.printBattleshipBoard(board_subsea, board_surface)
	#Check whether computer ships are all sink.
	if (len(computer_submarine) == 0) and (len(computer_carrier) == 0):
		print("Congratulations!!! You win!!!")
		break
	else: 
		print("Submarine:", 3 - len(computer_submarine), "/3; Carrier:", 4 - len(computer_carrier), "/4.")
	
	#Computer Attack
	for attack in Attack.AttackArea(Attack.ComputerAttack()):
		if attack in user_ship:
			user_ship.remove(attack)
	if len(user_ship) == 0:
		("Your ships are destroyed! Game Over! Good luck next time!")
		break
	else:
		print("Computer's turn over. You survived!\n")
