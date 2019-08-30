class User:

	def __init__(self, username, pin, balance=0):
		"""Creating a new user"""

		self.username = username
		self.pin = str(pin)
		self.balance = int(balance)
		self.__saveChanges()


	def printinfo(self):
		"""Printing out the user information"""

		print(f'\nUser Information:')
		print('=========================')
		print(f'Username: {self.username}')
		print(f'Account Balance: ${self.balance}\n')

	
	def checkBalance(self):
		"""Printing out the balance inforamtion"""

		print(f'\nCurrent Balance: ${self.balance}\n')
		
	
	def deposit(self):
		"""Deposit money to the user's account"""

		suma = int(input('\nEnter the sum of money that you would want to deposit: '))
		self.balance += suma
		print(f'Your account balance has been increased by ${suma}.')
		print(f'Current Balance: ${self.balance}\n')
		self.__saveChanges()


	def withdraw(self):
		"""Withdraw money from the user's account"""

		suma = int(input('\nEnter the sum of money that you would want to withdraw: '))
		
		# If the current balance is less than the sum which the user wnts to withdraw, inform the user and stop the process
		# else decrease the account balance by the sum that has been withdrawn and save the changes.
		if self.balance < suma:
			print('You don\'t have enough money to withdraw!\n')
		else:
			self.balance -= suma
			print(f'You have successfuly withrawn ${suma}.')
			print(f'Current Balance: ${self.balance}\n')
			self.__saveChanges()


	def changePin(self):
		"""Changing the user's pin code"""

		# Prompt the user for his/her current pin code
		while True:
			pin = input('\nCurrent pin code: ')
			if pin == self.pin:
				break
			else:
				print('The pin code that you entered doesn\'t match your actual pin code!')

		# Prompt the user for his/her new pin code and than ask for confirmation
		# When the user enters two matching pin codes, update the pin code and save the changes
		while True:
			newpin = input('New pin code: ')
			confirmation = input('Confirm the new pin code: ')
			if newpin == confirmation:
				self.pin = str(newpin)
				self.__saveChanges()
				print('\nYour pin code has been successfully changed!\n')
				break
			else:
				print('The two pin codes don\'t match!')


	def __saveChanges(self):
		"""Saving the changes and writing them in a txt file"""

		f = open(f'{self.username}.txt', 'w')
		f.write(f'Username: {self.username}\n')
		f.write(f'Pin: {self.pin}\n')
		f.write(f'Account Balance: {self.balance}\n')
		f.close()