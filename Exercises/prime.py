from math import sqrt

while True:
    num = input('input an positive integer: ')

    if num.isdigit() and int(num) > 1:
        num = int(num)
        prime = True
        hlf = int(num / 2)
        
        if hlf == 2:
            prime = False
        else:
            for i in range(2, int(sqrt(num))):
                if num % i == 0:
                    prime = False
                    break
        
    if prime:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')
    
    while True:
        ans = str(input('Try another number? (Y, N): '))
        if ans.upper() == 'Y' and len(ans) == 1:
            print('------------------------------')
            break
        elif ans.upper() == 'N' and len(ans) == 1:
            print('------------------------------')
            print('thanks for using our program')
            print('------------------------------')
            break
        elif ans.upper() != 'Y' and ans.upper() != 'N':
            print('--------------------------------------------')
            print('Error, only values among (Y, N) are valid!')
            print('--------------------------------------------')
            continue
    
    if ans.upper() == 'N':
        break