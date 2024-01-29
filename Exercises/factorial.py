def fact(num):
    if num != 0 and num > 1:
        return num * fact(num - 1)
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    elif num < 0:
        return 'only positive integers!'

while True:
    while True:
        num = input('type a number: ')

        if num.isdigit():
            num = int(num)
            print(fact(num))
            break
        else:
            print('--------------------------------------------------------------')
            print('Error, only positive integers are allowed! Try another number!')
            print('--------------------------------------------------------------')
            continue
    
    while True:
        ans = input('Try another number? (Y, N): ')

        if ans.upper() == "Y" and len(ans) == 1:
            print('----------------------------')
            break
        elif ans.upper() == 'N' and len(ans) == 1:
            print('----------------------------')
            print('thanks for using our program')
            print('----------------------------')
            break
        else:
            print('----------------------------------------------------')
            print('Error, only values among (Y, N) are valid! Try again')
            print('----------------------------------------------------')
            continue
    
    if ans.upper() == 'N':
        break