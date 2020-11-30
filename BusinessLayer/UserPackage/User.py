class User:
    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

    def Login(self, password):
        return self.password == password

    def ChangePass(self, oldPass, newPass):
        if self.password == oldPass:
            self.password = newPass
        else:
            print("The old password is wrong")

    def ChangeName(self, newName):
        self.username = newName