from collections import Counter
from math import sqrt

def average(list):
    soma = 0
    for i in list:
        soma += i
    return soma / len(list)


def median(list):
    list = sorted(list)
    result = 0
    if (len(list) % 2) == 0:
        result = (list[int(len(list) / 2)]) + (list[int(len(list) / 2) - 1])
        result = result / 2
    else:
        result = list[int(len(list) / 2)]
    return result


def fashion(list):
    count = Counter(list)
    moda = [i for i, f in count.items() if f== max(count.values())]
    return moda

def stdDeviation(list):
    avg = average(list)
    variancy = 0
    variancyL = []
    desv = 0
    desvL = []

    for i in list:
        variancy = avg - i
        if variancy < 0:
            variancy *= -1
        variancyL.append(variancy)
    
    for i in variancyL:
        desvL.append(i**2)
    
    desv = average(desvL)

    return sqrt(desv)


while True:
    numbers = []

    while True:
        quant = input('how many numbers do you wanna insert? ')

        if quant.isdigit():
            quant = int(quant)
            break
        else:
            print('-------------------------------------------')
            print('Error! only integers are allowed. Try again')
            print('-------------------------------------------')
    
    for i in range(0, quant):
        num = int(input(f'insert the {i} number: '))
        numbers.append(num)
    
    print('-------------------------------------------')
    print(f'average: {average(numbers)}')
    print(f'median: {median(numbers)}')
    print(f'fashion: {fashion(numbers)}')
    print(f'standard deviation: {stdDeviation(numbers):.2f}')
    print('-------------------------------------------')

    while True:
        ans = input('try again? (Y, N): ')

        if ans.upper() == 'Y' and len(ans) == 1:
            print('-------------------------------------------')
            break
        elif ans.upper() == 'N' and len(ans) == 1:
            break
        else:
            print('-------------------------------------------')
            print('only values among (Y, N) are valid!')
            print('-------------------------------------------')
    
    if ans.upper() == 'N':
        print('-------------------------------------------')
        print('thanks for using our program')
        print('-------------------------------------------')
        break