import random

def dice_roller():
    dice_roll_list = []
    for number in range(3):
        dice_roll_list.append(random.randint(1,6))
    print(dice_roll_list)
    return(dice_roll_list)

player_1_wins = 0
player_2_wins = 0
rounds_played = 0

while player_1_wins < 3 and player_2_wins < 3:
    rounds_played += 1
    player_1_roll_total = sum(dice_roller()) 
    player_2_roll_total = sum(dice_roller()) 
    if player_1_roll_total > player_2_roll_total:
        print("Player 1 won this round!")
        player_1_wins += 1
    elif player_1_roll_total < player_2_roll_total:
        print("Player 2 won this round!")
        player_2_wins += 1
    elif player_1_roll_total == player_2_roll_total:
        print("This round was a draw.")
        player_1_wins += 1
        player_2_wins += 1

print("The game consisted of {} rounds.".format(rounds_played))

if player_1_wins > player_2_wins:
    print("Player 1 is the winner, scoring {} vs {}.".format(player_1_wins,player_2_wins))
elif player_2_wins > player_1_wins:
    print("Player 2 won the game, scoring {} vs {}.".format(player_2_wins,player_1_wins))
elif player_1_wins == player_2_wins:
    print("The game is a draw!")

print('Game over!')