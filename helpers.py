from user import User

def register():
	"""Register a new user"""
	
	# Prompt the new user for a username and check if the username is available
	while True:
		username = input('Username: ')
		
		# Try to open a .txt file named {username}.txt.
		# If the file is successfully opened, that means that the username is taken.
		try:
			f = open(f'{username}.txt')
			print('The username you entered is not available!\n')
		
		# If the username is available, prompt the user for a pin code and a confirmation of the pin.
		except:
			
			# Prompt the user for a pin code and a confirmation of the pin.
			while True:
				pin = input('Create a pin code for your account: ')
				confirmation = input('Confirm the pin code: ')
				if pin == confirmation:
					break
				else:
					print('The two pin codes don\'t match!')
			
			# Create the new user
			user = User(username, pin)
			break

	print('\nSuccessfully registered!\n')
	return user


def login():
	"""User login"""

	# Prompt the user for his/her username and check if it is valid
	while True:
		username = input('Username: ')
		
		# Try to open a .txt file named {username}.txt.
		# If the file is successfully opened, that means that the username is valid.
		try:
			f = open(f'{username}.txt')
			break
		except:
			print('Invalid username!')

	# Check the validity of the pin code
	while True:
		# Prompt the user for his/her pin code
		pin = input('Pin: ')
		
		# Find the pin code which is saved in the .txt file. It is stored on the line which starts with "Pin: "
		for line in f:
			line = line.strip()
			if not line.startswith('Pin: '):
				continue
			userpin = line[5:]
		
		if pin == userpin:
			break
		else:
			print('Invalid pin code!\n')

	# Extracting the account balance
	# The account balance is stored in the .txt file and it is found on the line which starts with "Account Balance: "
	f = open(f'{username}.txt')
	for line in f:
		line = line.strip()
		if not line.startswith('Account Balance: '):
			continue
		balance = line[17:]

	# Overwrite the user
	user = User(username, pin, balance)

	return user