import random,sys

# r>s  s>p p>r

#To keep track of number of Wins,Losse and Ties

print( 'ROCK , PAPER , SCISSOR')

wins =0
losses =0
ties=0

while True:
    print(f'Score : Wins - {wins} , Losses - {losses} , Ties - {ties}')

    # Player inpyt loop 
    while True:
        print("Enter your Move : (r) -> Rock , (p) -> Paper, (s) -> Scissor and (q) -> Quit")
        playerMove = input()

        if playerMove == 'q':
            sys.exit() #
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display player move
    if(playerMove == 'r'):
        print("ROCK versus ...")
    elif(playerMove == 'p'):
        print("PAPER versus ...")
    elif(playerMove == 's'):
        print("SCISSOR versus ...")    

    #Display computer choice
    randomNumber = random.randint(1,3)

    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSOR')

    #Check wins/losses

    if playerMove == computerMove:
        print("Tie")
        ties +=1
    elif (playerMove =='r' and computerMove =='s') or (playerMove =='s' and computerMove =='p') \
            or (playerMove =='p' and computerMove =='r'):
        print('You Won')
        wins +=1
    elif (playerMove =='r' and computerMove =='p') or (playerMove =='s' and computerMove =='r') \
            or (playerMove =='p' and computerMove =='s'):
        print('You Lose')
        losses +=1