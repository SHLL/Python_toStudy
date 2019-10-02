password_list = ['*#*#','12345']

def account_login():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]

        if password_correct:
            print('Login succress !')

        elif password_reset:
            new_password = input('Enter a new passwrod :')
            password_list.append(new_password)
            print('Password has changed successfully')
            account_login()
        else:
            print('Wrong password or invalid input!')
            tries = tries - 1
            print(tries,'times left')
    else:
        print('Your accunt has been suspended')
account_login()