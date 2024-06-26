import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter a of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be betetween 2-4. ")
    else: 
        print("Invalid, try again.")


max_score = 50
player_score = [0 for _ in range(players)] # Creates an empty list that stores the score according to thier number.

while max(player_score) < max_score:


    for player_idx in range(players):
        print("\nPlayer number",player_idx + 1, "your turn just started.")
        print("Your total score is:", player_score[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y/n)?").lower()
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! You are out!!!")
                current_score = 0
                break
            else:
                current_score += value
                print("Your rooled a:", value)

            print("Your score is:", current_score)

        player_score[player_idx] += current_score
        print("Your total score is:", player_score[player_idx])
