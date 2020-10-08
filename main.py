import random

randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'p'
elif randNo == 2:
    comp = 's'
elif randNo == 3:
    comp = 'r'

def playAgain():
    print()
    print()
    game()

def gameWin(comp, you):
    if comp == you:
        gameWin = None
    elif comp == 's':
        if you == 'r':
            gameWin = True
        elif you == 'p':
            gameWin = False
    elif comp == 'r':
        if you == 's':
            gameWin = False
        elif you == 'p':
            gameWin = True
    elif comp == 'p':
        if you == 's':
            gameWin = True
        elif you == 'r':
            gameWin = False
    else:
        gameWin = 'False'
    return gameWin


def game():
    print('Computer Turn: Write (r) For Rock, (p) For Paper, (s) Scissor: ')
    you = input('Your Turn: Write (r) For Rock, (p) For Paper, (s) Scissor: ')
    result = gameWin(comp, you)
    print(f'You chose {you}')
    print(f'Computer chose {comp}')
    if result == True:
        print('You Win!!!')
    elif result == False:
        print('You Lose!!!')
    elif result == None:
        print('The Game Is Tie!!!')
    inp = input('Press (q) For Quit Or (a) For Playing It Again: ')
    if inp == 'q':
        print('Thanks For Playing The Game')
    elif inp == 'a':
        playAgain()

game()
