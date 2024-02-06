import random

# r>s  s>p p>r
def play():
    user_move = input(" 'r' for Rock , 'p' for Paper, 's' for Scissors : ").lower()
    computer_move = random.choice(['r','p','s'])

    if user_move == computer_move:
        return "It\'s a Tie."
    
    if is_won(user_move,computer_move):
        return 'You won!'
    
    return 'You Lost!'
    

def is_won(player , opponent):
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
       or (player == 'p' and opponent == 'r') :
        return True
    
game_result = play()
print(game_result)