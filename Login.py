import re

def Login():
	#The users can try three times before the account is locked. Once the account is locked, 
	#the user has to answer question to activate the account, in our system, the question is date of birth.
	while True:
		Username = input("Username: ")
		with open('AccData.txt', 'a+') as myfile: 		#opens the file
			myfile.seek(0)
			data = myfile.read()
			data = re.split(',|\n', data)
			if Username in data:                   		#checks if such an account exists, and retrieves the password if it does
				index = data.index(Username)
				password = data[index+1]
				dateofbirth = data[index+2]
				chance = 2
				InputPassword = input("Password: ")
				while chance > 0:
					if InputPassword == '####':
						break
					elif InputPassword == password:
						print("Login Successfully!")
						return True
					else:
						chance = chance - 1
						print("Wrong password! Please try again!(Press '####' back to Username)")
						InputPassword = input("Password: ")
				if chance == 0:
					while True:
						Dateofbirth = input("The account is locked. Please enter your date of birth to activte(Press '####' back to Username):")
						if Dateofbirth == '####':
							break
						elif Dateofbirth == dateofbirth:
							print("Login Successfully!")
							return True
						else:
							print("The answer is wrong. Please try it again!")
							continue
			else:
				print("Username does not exist. Please try again again.")
				

if __name__ == '__main__':
	Login()
