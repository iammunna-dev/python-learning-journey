import random

'''
number= random.random()
if number>0.5:
    print("HEADS")
else:
    print("TAILS")
    '''


name=["Bob","RObby","Agustin","James","Arneld","Catey","Dawid","Jacob","Ernest","Mitchel"]

#1st option, this is kinda tough
'''
random_number=random.randint(0,9)
random_name=name[random_number]

print(random_name)

#2nd option, easier
print(random.choice(name))
'''

'''

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][3])
'''

import random

user_input= int(input("Enter 0 for ROCK, 1 for Paper and 2 for Scissors\n"))
random_computer_input=random.randint(0,2)


rock= ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper= ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors= ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if user_input>=0 and user_input<=2:
    if user_input==0:
        print("User Choose: ",rock)
    elif user_input==1:
        print("User Choose: ",paper)
    elif user_input==2:
        print("User Choose: ",scissors)
    if random_computer_input==0:
        print("Computer Choose: ",rock)
    elif random_computer_input==1:
        print("Computer Choose: ",paper)
    elif random_computer_input==2:
        print("Computer Choose: ",scissors)
    if user_input==random_computer_input:
        print("It's a Draw")
    if user_input==0 and random_computer_input==1:
        print("COMPUTER WON THE GAME")
    if user_input==1 and random_computer_input==0:
        print("HUMAN WON THE GAME")
    if user_input==0 and random_computer_input==2:
        print("HUMAN WON THE GAME")
    if user_input==2 and random_computer_input==0:
        print("COMPUTER WON THE GAME")
    if user_input==1 and random_computer_input==2:
        print("COMPUTER WON THE GAME")
    if user_input==2 and random_computer_input==1:
        print("HUMAN WON THE GAME")

else:
    print("Please enter correct number")

