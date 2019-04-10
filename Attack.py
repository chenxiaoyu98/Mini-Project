from pprint import pprint
import random
import string

def ComputerAttack():
	x = random.randint(0, 9)
	y = random.randint(0, 9)
	depth = random.randint(0, 1)
	return [x, y, depth]

def UserAttack():
	while True:
		try:
			row_str, col_str, depth_str = input("Enter the Attack Coordinate(E.g. A,4,1): ").split(',')
			row, col, depth = ord(row_str) - 65, int(col_str) - 1, int(depth_str)
			if (0 <= row < 10) and (0 <= col < 10) and (0 <= depth <= 1):
				return [row, col, depth]
			else:
				print("Please enter the correct coordinate using the format within range(row, col, depth). E.g. A,4,1")
		except (ValueError, TypeError):
			print("Please enter the correct coordinate using the format(row, col, depth). E.g. A,4,1")


def AttackArea(C):
	B = tuple(C)
	coordList = []
	coordList.append(B)

	C1 = list(B)
	#print(C1)
	if C1[0] != 9:
		C1[0] = B[0] + 1
		C1 = tuple(C1)
		coordList.append(C1)

	C2 = list(B)
	#print(C2)
	if C2[0] != 0:
		C2[0] = B[0] - 1
		C2 = tuple(C2)
		coordList.append(C2)

	C3 = list(B)
	if C3[1] != 9:
		C3[1] = B[1] + 1
		C3 = tuple(C3)
		coordList.append(C3)

	C4 = list(B)
	if C4[1] != 0:
		C4[1] = B[1] - 1
		C4 = tuple(C4)
		coordList.append(C4)

	C5 = list(B)
	if C5[0] != 9 and C5[1] != 9:
		C5[0] = B[0] + 1
		C5[1] = B[1] + 1
		C5 = tuple(C5)
		coordList.append(C5)

	C6 = list(B)
	if C6[0] != 0 and C6[1] != 0:
		C6[0] = B[0] - 1
		C6[1] = B[1] - 1
		C6 = tuple(C6)
		coordList.append(C6)

	C7 = list(B)
	if C7[0] != 0 and C7[1] != 9:
		C7[0] = B[0] - 1
		C7[1] = B[1] + 1
		C7 = tuple(C7)
		coordList.append(C7)

	C8 = list(B)
	if C8[0] != 9 and C8[1] != 0:
		C8[0] = B[0] + 1
		C8[1] = B[1] - 1
		C8 = tuple(C8)
		coordList.append(C8)
	
	return coordList


if __name__ == '__main__':
	print(AttackArea([0,0,0]))
	print(AttackArea([9,5,0]))
