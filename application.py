from user import User
from helpers import register, login
from time import sleep


print()
print('**** E-ATM ****')
print()

# The user chooses whether to register or sign in
while True:		
	try:
		option = int(input('\nWhat do you want to do?\n1) Register\n2) Sign in\n'))
	except:
		option = 0
	if option == 1 or option == 2:
		break

if option == 1:
	user = register()
else:
	user = login()

# The user chooses an option:
# 1) See user information
# 2) Balance check
# 3) Deposit money
# 4) Withdraw money
# 5) Change pin code
# 6) Exit
options = '\nWhat do you want to do?\n1) SEE USER INFO\n2) CHECK BALANCE\n3) DEPOSIT MONEY\n4) WITHDRAW MONEY\n5) CHANGE PIN\n6) EXIT\n'

while True:
	try:
		option = int(input(options))
	except:
		option = -1
	if option == 1 or option == 2 or option == 3 or option == 4 or option == 5 or option == 6:
		break

if option == 6:
	print('\nGOODBYE!\n')
	sleep(1)
	exit()
else:
	while option != 6:
		if option == 1:
			user.printinfo()
			input('Press ENTER to continue...')
		elif option == 2:
			user.checkBalance()
			input('Press ENTER to continue...')
		elif option == 3:
			user.deposit()
			input('Press ENTER to continue...')
		elif option == 4:
			user.withdraw()
			input('Press ENTER to continue...')
		elif option == 5:
			user.changePin()
			input('Press ENTER to continue...')
		option = int(input(options))

	print('\nGOODBYE!\n')
	sleep(1)
	exit()