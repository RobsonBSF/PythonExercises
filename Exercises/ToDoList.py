from os import remove

#--- Functions ---#
def CreateList(fileName):
    with open(fileName, 'w') as file:
        file.write('--- TodoList ---\n')

def readList(fileName):
    with open(fileName) as file:
        content = file.read()
    return content

def insertList(fileName, insert):
    with open(fileName, 'r') as file:
        content = file.read()

    with open(fileName, 'w') as file:
        file.writelines(content +'\n' + insert)

def removeItem(fileName, removeI):
    with open(fileName, 'r') as file:
        content = file.read()
        content = content.replace(removeI, '')

    with open(fileName, 'w') as file:
        file.write(content)

def deleteList(fileName):
    remove(fileName)

def sisMsg(msg):
    print('--------------------------------')
    print(msg)
    print('--------------------------------')


#--- Main program ---#
print('--------------------------------')
print('--- To do List ---')

while True:
    print('--------------------------------')
    ans = input('What you wanna do?\n[1] Create a new List\n[2] Open a List\n[3] Exit\nChoice: ')
    print('--------------------------------')

    if ans.isdigit() and int(ans) == 1:
        choice1 = str(input('New File name (ex: test.txt): '))

        CreateList(choice1)

    elif ans.isdigit() and int(ans) == 2:
        while True:
            check = True
            try:
                fileName = str(input('[0] Return\nFile name (ex: test.txt): '))
                
                if fileName.isdigit() and int(fileName) == 0:
                    print('--------------------------------')
                    break
                else:
                    print('--------------------------------')
                    readList(fileName)
                
                while check:
                    choice2 = input('[1] Update List\n[2] View List\n[3] Exit\nChoice: ')
                    print('--------------------------------')

                    if choice2.isdigit() and int(choice2) == 1:
                        while True:
                            choice21 = input('[1] Insert Item\n[2] Remove Item\n[3] Delete List\n[4] Return\nChoice: ')
                            print('--------------------------------')

                            if choice21.isdigit() and int(choice21) == 1:
                                while True:
                                    insert = input('[0] Return\nItem to insert: ')
                                    if insert.isdigit() and int(insert) == 0:
                                        print('--------------------------------')
                                        break
                                    else:
                                        insertList(fileName, str(insert))
                                        print('--------------------------------')
                                        break

                            elif choice21.isdigit() and int(choice21) == 2:
                                while True:
                                    try:
                                        removeI = str(input('[0] Return\nItem to remove: '))
                                        if removeI.isdigit() and int(removeI) == 0:
                                            print('--------------------------------')
                                            break
                                        else:
                                            removeItem(fileName, removeI)
                                            print('--------------------------------')
                                            break
                                    except:
                                        sisMsg('item does not exists!, try again')

                            elif choice21.isdigit() and int(choice21) == 3:
                                deleteList(fileName)
                                print('--------------------------------')
                                check = False
                                break
                            elif choice21.isdigit() and int(choice21) == 4:
                                print('--------------------------------')
                                break
                            else:
                                sisMsg('Only integers among (1, 2, 3) are valid! Try again')

                    elif choice2.isdigit() and int(choice2) == 2:
                        print('--------------------------------')
                        print(readList(fileName))
                        print('--------------------------------')
                    elif choice2.isdigit() and int(choice2) == 3:
                        break
                    else:
                        sisMsg('Only integers among (1, 2, 3) are valid! Try again')
                break
            except:
                sisMsg('Incorrect file name! Try again')

    elif ans.isdigit() and int(ans) == 3:
        sisMsg('Thanks for using our program!')
        break
    else:
        sisMsg('Only integers among (1, 2, 3) are valid! Try again')