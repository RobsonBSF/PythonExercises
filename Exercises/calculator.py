def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

while True:
    while True:
        num1 = input('first number: ')
        num2 = input('second number: ')

        if num1.isdigit() and num2.isdigit():
            num1 = float(num1)
            num2 = float(num2)
            break
        else:
            print('\nOnly numbers allowed, try again!\n')
    
    while True:
        op = str(input('operation (+, -, *, /): '))

        if op in '+-*/' and len(op) == 1:
            break
        else:
            print('\nInvalid operation! Please enter a single character among +, -, *, or /\n')
    
    if op == '+':
        print(add(num1, num2))
    elif op == '-':
        print(subtract(num1, num2))
    elif op == '*':
        print(multiply(num1, num2))
    elif op == '/':
        if num2 == 0:
            print('\nzero division error!\n')
        else:
            print(divide(num1, num2))
    
    cont = str(input('calculate another number? (Y, N): '))
    if cont.upper() == 'N':
        print('------------------------------------')
        print('thanks for using our program!')
        print('------------------------------------')
        break
    elif cont.upper() == 'Y':
        print('------------------------------------')
        continue