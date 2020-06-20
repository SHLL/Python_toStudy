def account():
    password = input('password:')
    passowrd_correct = password == '12345'
    if passowrd_correct:
        print('Login success!')
    else:
        print('woring password of invalid input!')
        account()

account()