# Day 3 Task：Create a game based on instruction

def treasure_island(game_start):
    direction = input(
        "Welcome to Treasure Island. Your mission is to find the treasure.\n You are at crossroad.First Question: Left or right? Please enter l or r. ").strip().lower()
    if direction == "l":
        print("Smart move.")
        action = input(
            "Second Question: Swim or Wait? Enter S for Swim, W for wait ").strip().lower()
        if action == "w":
            print(
                "Move forward. There is three big door in front of you. Each door has diffrent color.")
            chioce = input(
                "Which door? Please enter R for Red, B for Blue, Y for Yelow. ").strip().lower()
            if chioce == "r":
                print("Burned by fire.\n Game Over.")
            elif chioce == "b":
                print("Eaten by beasts.\n Game Over.")
            elif chioce == "y":
                print("Congrats! You win!")
            else:
                print("Game Over.")
        else:
            print("Attaked b y trout.\n Game Over.")
    else:
        print("Fall into a hole.\n Game Over.")


# Intruduction
game_start = input("Hi, Do you want play games? Y or N: ").strip().upper()

if game_start == "Y":
    treasure_island(game_start)
else:
    print("Bye! See you next time.")
