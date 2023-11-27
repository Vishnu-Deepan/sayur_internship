# Problem #3
# Its is a single player game where the user starts with 0 points. User keeps rolling the 
# dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
#  added. If the number is odd, then if the number is 1,3 then the user has to jump. 
#  If the number is 5, then 3 points are added. The game ends when the user has 50 points.


import random

def dice_game():
    points = 0

    while points < 50:
        roll = random.randint(1, 6)

        if roll == 0:
            print("Game ends. You rolled 0.")
            break
        elif roll % 2 == 0:
            points += 2
        elif roll in [1, 3]:
            print(f"You rolled {roll}. Jump!")
        elif roll == 5:
            points += 3

        print(f"Rolled: {roll}, Points: {points}")

    if points >= 50:
        print("Congratulations! You reached 50 points.")

dice_game()
