def CheckOverlapping(carrier, submarine):
	if submarine[1][2] == 1:
		for element in submarine:
			if element in carrier:
				return False
		return True
	else:
		return True

def Usersubmarine():
	#Promote user to place a submarine.
	print("Placing a Submarine (Take up 3 continuous units and can be placed in depth: 0,1).")
	
	#Choose the orientation.
	submarine_orientation_str = input("Enter the orientation of submarine (0 for vertical, 1 for horizontal): ")
	while True:
		try:
			submarine_orientation  = int(submarine_orientation_str)
			if 0 <= submarine_orientation <= 1:
				break
			else:
				submarine_orientation_str = input("Please choose 0 or 1.\nEnter the orientation of submarine: ")
		except ValueError:
			submarine_orientation_str = input("Please choose 0 or 1.\nEnter the orientation of submarine:")
			
	#Enter the first coordinate.
	print("\nPlease enter the coordinates following this format (row, col, depth). E.g. A,4,1")
	print("Note: depth = 0 represents the subsea layer; depth = 1 represents the surface level.")
	if submarine_orientation == 0:
		print("The 1st coordinate is the forepart of the submarine. Please enter row from A to G, col from 1 to 10.\n")
	else: 
		print("The 1st coordinate is the forepart of the submarine. Please enter row from A to J, col from 1 to 7.\n")
	
	while True:
		try:
			row_str, col_str, depth_str = input("Enter 1st Coordinate: ").split(',')
			row, col, depth = ord(row_str) - 65, int(col_str) - 1, int(depth_str)
			if (submarine_orientation == 0) and (0 <= row < 7) and (0 <= col < 10) and (0 <= depth <= 1):
				submarine = [(row, col, depth),(row + 1, col, depth),(row + 2, col, depth)]
				return submarine
			elif (submarine_orientation == 1) and (0 <= row < 10) and (0 < col < 7) and (0 <= depth <= 1):
				submarine = [(row, col, depth),(row, col + 1, depth),(row, col + 2, depth)]
				return submarine
			else:
				print("Please enter the correct coordinate using the format within range(row, col, depth). E.g. A,4,1")
		except (ValueError, TypeError):
			print("Please enter the correct coordinate using the format(row, col, depth). E.g. A,4,1")
	

def Usercarrier(submarine):
	#Promote user to place a carrier.
	print("Placing a Carrier (Take up 4 continuous units and can only be placed in depth: 1).")
		
	#Choose the orientation.
	carrier_orientation_str = input("Enter the orientation of carrier (0 for vertical, 1 for horizontal): ")
	while True:
		try:
			carrier_orientation  = int(carrier_orientation_str)
			if 0 <= carrier_orientation <= 1:
				break
			else:
				print("Please choose 0 or 1.\nEnter the orientation of carrier: ")
		except ValueError:
				carrier_orientation_str = input("Please choose 0 or 1.\nEnter the orientation of carrier:")
				
	#Enter the first coordinate.
	print("\nThe carrier can only be placed in the surface level.")
	print("Please enter the coordinates following this format (row, col). E.g. A,4.")
	if submarine[1][1] == 1:
		print("Note: Within the same layer, ships cannot be placed on one another!")
	if carrier_orientation == 0:
		print("The 1st coordinate is the forepart of the carrier. Please enter row from A to G, col from 1 to 10.")
	else: 
		print("The 1st coordinate is the forepart of the submarine. Please enter row from A to J, col from 1 to 7.")
	
	while True:
		try:
			row_str, col_str= input("Enter 1st Coordinate: ").split(',')
			row, col = ord(row_str) - 65, int(col_str) - 1
			if (carrier_orientation == 0) and (0 <= row < 7) and (0 <= col < 10):
				carrier = [(row , col, 1),(row + 1, col, 1),(row + 2, col, 1),(row + 3, col, 1)]
				if CheckOverlapping(carrier, submarine):
					return carrier
				else:
					print("Within the same layer, ships cannot be placed on one another! Try it again!\n")
			elif (carrier_orientation == 1) and (0 <= row < 10) and (0 <= col < 7):
				carrier = [(row, col, 1),(row, col + 1, 1),(row, col + 2, 1),(row, col + 3, 1)]
				if CheckOverlapping(carrier, submarine):
					return carrier
				else:
					print("Within the same layer, ships cannot be placed on one another! Try it again!\n")
			else:
				print("Please enter the correct coordinate using the format within range(row, col, depth). E.g. A,4,1\n")
		except (ValueError, TypeError):
			print("Please enter the correct coordinate using the format(row, col, depth). E.g. A,4,1\n")

	
def Userships():
	submarine = Usersubmarine()
	print("\n")
	carrier = Usercarrier(submarine)
	return submarine, carrier


if __name__ == '__main__':
	submarine, carrier = Userships()
	print(submarine, carrier)
