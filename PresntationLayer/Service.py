from PresntationLayer.UserService import UserService


class Service:

    def __init__(self):
        self.us = UserService()

    def Login(self, email, password):
        self.us.Login(email, password)

    def Register(self, email, password, username):
        self.us.Register(email, password, username)

    def Logout(self):
        self.us.Logout()

    def ChangePass(self, oldPass, newPass):
        self.us.ChangePass(oldPass, newPass)

    def ChangeName(self, newName):
        self.us.ChangeName(newName)
