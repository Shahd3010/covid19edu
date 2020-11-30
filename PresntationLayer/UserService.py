from BusinessLayer.UserPackage.UserController import UserController


class UserService:
    def __init__(self):
        self.uc = UserController()

    def Login(self, email, password):
        self.uc.Login(email, password)

    def Register(self, email, password, username):
        self.uc.Register(email, password,username)

    def Logout(self):
        self.uc.Logout()

    def ChangePass(self, oldPass, newPass):
        self.uc.ChangePass(oldPass, newPass)

    def ChangeName(self,newName):
        self.uc.ChangeName(newName)