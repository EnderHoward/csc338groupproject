#login_client - Client side login functions


def getCreds():
	name = input('Enter user name: ')
	password = input('Enter password: ')
	userData = name + ':' + password
	return userData
	