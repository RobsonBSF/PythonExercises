from random import randint

def printWord(wrd):
    for i, j in enumerate(wrd):
        print(f'{wrd[i]}', end=' ')

words = ['happy', 'jump', 'play', 'drive', 'falcon', 'dog', 'eagle', 'car', 'building', 'rock']

while True:
    word = words[randint(0, (len(words) - 1))].lower()
    word = list(word)
    
    wordAns = ['_' for i in word]
    chances = 6

    while True:
        correct = False

        print('\n-----------------------------')
        print(f'chances: {chances}')

        while True:
            guess = str(input('guess a letter: '))

            if guess.isdigit():
                print('-----------------------------')
                print('Only letters alowed! try again')
                print('-----------------------------')
            else:
                break

        for i, j in enumerate(word):
            if guess.lower() == j:
                correct = True
                wordAns[i] = word[i]

        if wordAns == word:
            printWord(wordAns)
            print('\n-----------------------------')
            print('You Win!')
            break

        if not correct:
            chances -= 1
        
        if chances == 0:
            print('\n-----------------------------')
            print('the word was: ')
            printWord(word)
            print('\n-----------------------------')
            print('Out of chances...')
            break

        printWord(wordAns)
    
    print('-----------------------------')
    ans = str(input('Try again? (Y, N): '))
    print('-----------------------------')

    if ans.upper() == 'N':
        print('-----------------------------')
        print('thanks for using our program!')
        print('-----------------------------')
        break