import random
'''
#Heads Tails Generator
head_or_tail=random.randint(0,1)
if head_or_tail==0:
    print("HEADS")
else:
    print("TAILS")

friends=["Angela","Alexa","Raisey","Nikola","Frederick","Holmes","Abbey","Mbappe","Cristiano"]
who_will_pay=random.randint(0,8)
print(friends[who_will_pay])


##BETTER ALTERNATIVE TO THIS
friends=["Angela","Alexa","Raisey","Nikola","Frederick","Holmes","Abbey","Mbappe","Cristiano"]
year=12,13,14,15
print(random.choice(friends))
print(random.choices(friends,k=3))

'''

##ROCK PAPER SCISSORS
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


user=int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer=random.randint(0,2)
print("You Choose:")


if user==0:
    print(rock)
elif user==1:
    print(paper)
elif user==2:
    print(scissors)
else:
    print("Please Enter Correct Number")

print("Computer Choose:")


if computer==0:
    print(rock)
elif computer==1:
    print(paper)
else:
    print(scissors)

##Determining Winner
if user==0 and computer==2 or user==1 and computer==0 or user==2 and computer==1:
    print("You WIN!")

elif user==computer:
    print("It's a DRAW")
else:
    print("Computer WINS!")