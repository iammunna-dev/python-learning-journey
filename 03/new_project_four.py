print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
print("Welcome to Treasure Island\nYour mission is to find treasure")
left_right=input("Where you want to go? L for Left and R for Right:\n").lower()


if left_right=="l":
    print("You have come to a river. Do you want to Swim or wait for a Boat?")
    swim_boat=input("Type Swim or Wait:\n").lower()
    if swim_boat=="swim":
        print("Attact by trout\nGAME OVER")
    elif swim_boat=="wait":
        print("There are three doors open for you.")
        three_doors=input("Which way you want to go? RED, BLUE or YELLOW?:\n").lower()
        if three_doors=="red":
            print("Burned by Fire\nGAME OVER")
            exit()
        elif three_doors=="blue":
            print("Eaten by Beasts\nGAME OVER")
            exit()
        elif three_doors=="yellow":
            print("Congratulations!!\n YOU  WIN!!")
        else:
            print("Please Enter Correct Command")
            exit()


    else:
        print("Please enter correct command")
        exit()





elif left_right=="r":
    print("Game Over")
    exit()
else:
    print("Please type R or L")