import random

def Computerships():
	#Generate computer's Submarine
	#For layer: 0 represents the subsea layer, 1 represents the surface layer.
	#For orientation:0 represents horizontal, 1 represents vertical.
	submarine_layer = random.randrange(2)
	submarine_orientation = random.randrange(2)
	submarine_forepart_x = random.randrange(8)
	submarine_forepart_y = random.randrange(10)
	if submarine_orientation == 1:
		submarine = [(submarine_forepart_x, submarine_forepart_y, submarine_layer),\
			(submarine_forepart_x + 1, submarine_forepart_y, submarine_layer),\
			(submarine_forepart_x + 2, submarine_forepart_y, submarine_layer)]
	else:
		submarine = [(submarine_forepart_y, submarine_forepart_x, submarine_layer),\
			(submarine_forepart_y, submarine_forepart_x + 1, submarine_layer),\
			(submarine_forepart_y, submarine_forepart_x + 2, submarine_layer)]

	#Generate computer's carrier
	while True:
		carrier_orientation = random.randrange(2)
		carrier_forepart_x = random.randrange(7)
		carrier_forepart_y = random.randrange(10)
		if carrier_orientation == 0:
			carrier = [(carrier_forepart_x, carrier_forepart_y, 1),\
				(carrier_forepart_x + 1, carrier_forepart_y, 1),\
				(carrier_forepart_x + 2, carrier_forepart_y, 1),\
				(carrier_forepart_x + 3, carrier_forepart_y, 1)]
		else:
			carrier = [(carrier_forepart_y, carrier_forepart_x, 1),\
				(carrier_forepart_y, carrier_forepart_x + 1, 1),\
				(carrier_forepart_y, carrier_forepart_x + 2, 1),\
				(carrier_forepart_y, carrier_forepart_x + 3, 1)]
		
		#Check if there is any overlapping.
		if submarine_layer == 1:
			for element in submarine:
				overlapping = False
				if element in carrier:
					overlapping = True
					break
			if overlapping == False:
				return submarine, carrier
		else:
			return submarine, carrier
				

if __name__ == '__main__':
	submarine, carrier = Computerships()
	print(submarine)
	print(carrier)
