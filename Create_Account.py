import re

def CreateAccount():
	Username = input("Username: ")
	with open('AccData.txt','a+') as myfile: #opens file and reads the the data into data as string
		myfile.seek(0)
		data = myfile.read()
		data = re.split(',|\n',data)         #splits the string into a list with them being seperated by \n and commas
	while Username in data:
		print("The username already exists! Please enter a new one!")
		Username = input("Username: ") 
	else:
		Password = CreatePassword(Username)
		Dateofbirth = CreateDateofbirth()
		with open('AccData.txt','a+') as myfile: #writes all the data into text file
			myfile.write(Username)
			myfile.write(",")
			myfile.write(Password)
			myfile.write(",")
			myfile.write(Dateofbirth)
			myfile.write('\n')
		print("Account details saved.")
		return

def CreateDateofbirth():
	while True:
		DateOfBirth = input("Date of Birth(DDMMYYYY): ")
		if DateOfBirth.isdigit() and len(DateOfBirth) == 8:
			return DateOfBirth
		else:
			print("Please enter 8 digits only!")

def CreatePassword(Username):
	while True:
		Password = input("Password: ")
		#Check the password length.
		if len(Password) <= 8:
			print("The length of password must be more than 8 chracters.")
			continue
		#Check if there is at least one uppercase letter, one lowercase letter, one digit and one punctuation.
		upper = 0
		lower = 0
		digit = 0
		for element in Password:
			if element.isupper():
				upper += 1
			if element.islower():
				lower += 1
			if element.isdigit():
				digit += 1
		punctuation = len(Password) - upper - lower - digit
		if upper == 0 or lower == 0 or digit == 0 or punctuation == 0:
			print("The password should contain at least one uppercase letter, one lowercase letter, one digit and one punctuation.")
			continue
		#Check if the password contains the username (case insensitive).
		Username_lower = Username
		Password_lower = Password
		Username_lower.lower()
		Password_lower.lower()
		if Username_lower in Password_lower:
			print("The password should not contain username.")
			continue
		return Password

if __name__ == '__main__':
	CreateAccount()
	
