print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
left_or_right=input("Do you want to go left or right. Write l for left or r for right: \n")
if left_or_right=="l":
    print("You have come to a river")
    swim_or_wait=input("Do you want to swim or wait here for boat?")
    if swim_or_wait=="wait":
        print("You have passed the river and cove into a cave. Now here are three doors Red, Yellow, Green")
        door=input("Which door you want to go?")
        if door=="yellow":
            print("Congratulations! You have WON the Game")
        elif door=="green":
            print("Eaten by Beast\n GAME OVER")
        elif door=="green":
            print("Burned by fire\n GAME OVER")
        else:
            print("GAME OVER")
    else:
        print("You were attacket by crocodile \n GAME OVER")
else:
    print("Game Over")