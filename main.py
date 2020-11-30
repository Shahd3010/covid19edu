from PresntationLayer.Service import Service


def ProgramRun():
    s = Service()
    print('1.Login')
    print('2.Register')
    print('3.Logout')
    print('4.Change password')
    print('5.Change name')
    print('')
    choice = int(input('Enter a number: '))
    while choice != 6:
        if choice == 1:
            email1 = input('Enter email: ')
            password1 = input('Enter password: ')
            s.Login(email1, password1)
        elif choice == 2:
            email2 = input('Enter email: ')
            password2 = input('Enter password: ')
            username2 = input('Enter username: ')
            s.Register(email2, password2, username2)
        elif choice == 3:
            s.Logout()
        elif choice == 4:
            passwordold = input('Enter old password: ')
            passwordnew = input('Enter new password: ')
            s.ChangePass(passwordold, passwordnew)
        elif choice == 5:
            username5 = input('Enter username: ')
            s.ChangeName(username5)
        else:
            print('Enter another number')
        choice = (input('Enter a number: '))


if __name__ == '__main__':
    ProgramRun()
