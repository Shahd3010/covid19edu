from BusinessLayer.UserPackage.User import User
from DataAccessLayer.DataController import DataController
from DataAccessLayer.Object.User import User as dal


class UserController:
    def __init__(self):
        self.user = None
        self.users = {}
        self.dc = DataController()
        # calling the dc.get() to get the data from the database and filling the users

    def Login(self, email, password):
        if email not in self.users:
            print("There is no user such as that")
        else:
            if self.user is None:
                if self.users[email].Login(password):
                    self.user = self.users[email]
                    print("The user is active")
                else:
                    print("The username or the password is wrong")
            else:
                print('There is active user')

    def Register(self, email, password, username):
        if self.user is not None:
            print('There is no active user')
        else:
            if self.user not in self.users:
                if len(password) > 5 and any(char.isdigit() for char in password):
                    self.users[email] = User(email, password, username)
                    print("The user is registered")
                    self.dc.Add(self.ToDalObj(self.users[email]))
                else:
                    print("The password must contain at least 6 characters and at least one number")
            else:
                print("There is already a user with this email")

    def Logout(self):
        if self.user is not None:
            self.user = None
            print("The user is offline")
        else:
            print('There is no user active')

    def ChangePass(self, oldPass, newPass):
        if self.user is not None:
            self.user.ChangePass(oldPass, newPass)
            print("Password is changed")
            self.dc.Update(self.ToDalObj(self.user))
        else:
            print('There is no user active')

    def ChangeName(self, newName):
        if self.user is not None:
            self.user.ChangeName(newName)
            print("Name is changed")
            self.dc.Update(self.ToDalObj(self.user))
        else:
            print('There is no user active')

    def ToDalObj(user):
        return dal(user.email, user.password, user.username)
