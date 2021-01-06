# if i save my game it shoud be save the score with player name.
# create a player with a rolling dice, for that we will use random int generator
# if the random number is 3 the game shoud stop and high score shoud be stored int  the file.


import random
scorelist = {}
index = 0
def luckGame(player):
    score = 0
    global index
    global scorelist
    for i in range(0,10):
        dice = random.randint(1, 5)
        if (dice == 3):
            scorelist[str(player)] = score
            print("you are done\n Next Player's Turn" )
            index = index + 1
            print(index)
            if index < 4:
                start() 
            else:
                printScore()
                exit()

        else:
            print(f'roundScore = {dice}')
            score += dice
            print(f'player - {player}  score - {score}')

def start():
    name = input('\nEnter Player Name To Play or 5 to stop the game: ')
    if name == '5':
        printScore()
        exit()
    else:
        name = name.casefold()       
        luckGame(name)
               

def printScore():
    with open('game.txt', 'a') as f:
        f.write(f'\n {str(scorelist)}')
    print(scorelist)
start()
