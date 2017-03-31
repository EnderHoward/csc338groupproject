#login_server - Server side login functions

#Global data file name
USER_DATA_FILE = 'users.dat'


#Takes a list of user data and writes it to the file
#userData format: ["name", "password"]
def createUser(userData):
    with open(USER_DATA_FILE, "r+") as file:
        len(file.readlines())
        file.write("%s:%s\n" % (userData[0], userData[1]))

#Reads all users from user data file and returns them into a list
def readUserList():
    with open(USER_DATA_FILE, "r") as file:
        userList = file.readlines()
        userList = [line.strip('\n') for line in userList]
        return userList

#Checks user credentials. Returns 0 if credentials match OR if no user by that name exists, one is created.
#Returns 1 if password does not match for the username given
#userLogin format: ["name", "password"]
def signIn(userLogin):
	userList = readUserList()
	for user in userList:
		name,pword = user.split(":")
		if (userLogin[0] == name):
			if (userLogin[1] == pword):
				return 0
			else:
				return 1	
	createUser(userLogin)
	return 0
		