import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} : "))

        if guess < random_number:
            print("Sorry guess again.Too low.")
        elif guess > random_number:
            print("Sorry guess again.Too High.")
        
    print(f"Congrats , You have successfully Guessed the random Number {random_number} correctly. ")


# In this computer will guess our number 

def select_user_number(x):
    user_num = int(input(f'Input Your Secret Number between 1 to {x} : '))


def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low # could also be high ie low = high
        
        feedback = input(f"Is {guess} too High (H), too Low (L), or guessed correct (C) : ").lower()

        if feedback == 'h':
            high = guess-1
        elif feedback== 'l':
            low = guess + 1
          
    print(f'Yay! the Computer Guessed your number,{guess} correctly.')

def play_game(x):
    select_user_number(x)
    computer_guess(x)

play_game(20)