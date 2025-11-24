#2nd Attempt
#### (%) This is Modulo Operator = it gives the value of what is remainder after division
#print(10%3)

#ODD EVEN FINDER TOOL WITH CALCULATOR
'''
value_one=int(input("Please Enter first value : \n"))
value_two=int(input("Please Enter second value : \n"))
operator=input("Write A for Addition, D for Divison, S for Substraction, M for Multiplication :\n").upper()
if operator=="A":
    addition=value_one+value_two
    if addition%2==0:
        print(f"The ADDITION is {addition} and it is an EVEN Number")
    else:
        print(f"The ADDITION is {addition} and it is an ODD Number")
if operator=="D":
    division=value_one/value_two
    if division%2==0:
        print(f"The DIVISION is {division} and it is an EVEN Number")
    else:
        print(f"The DIVISION is {division} and it is an ODD Number")
    
if operator=="S":
    substraction=value_one-value_two
    if substraction%2==0:
        print(f"The SUBSTRACTION is {substraction} and it is an EVEN Number")
    else:
        print(f"The SUBSTRACTION is {substraction} and it is an ODD Number")
if operator=="M":
    multiplication=value_one*value_two
    if multiplication%2==0:
        print(f"The MULTIPLICATION is {multiplication} and it is an EVEN Number")
    else:
        print(f"The MULTIPLICATION is {multiplication} and it is an ODD Number")
else:
    print("Please Enter Correct Operator")

##BMI CALCULATOR
height= int(input("Enter your height in CM: \n"))
height_in_meters=height/100
weight= int(input("Enter your weight in KG: \n"))
bmi=weight/height_in_meters**2
if bmi<18.5:
    print(f"Your BMI is {bmi:.2f} and you are UNDERWEIGHT")
elif bmi>=18.5 and bmi<24.9:
    print(f"Your BMI is {bmi:.2f} and you have NORMAL weight")
else:
    print(f"Your BMI is {bmi:.2f} and you are OVERWEIGHT")


'''
''''
##ROLLER COASTER
age=int(input("Please Enter Your Age: \n"))
ticket=0
if age>12 and age<=55:
    if age>12 and age<18:
        ticket=10
        print(f"Welcome to our Fun Roller Coaster Rider.\nYour ticket price is {ticket} ")
    elif age>=18 and age<=25:
        ticket=15
        print(f"Welcome to our Fun Roller Coaster Rider.\nYour ticket price is {ticket} ")
    else:
        ticket=20
        print(f"Welcome to our Fun Roller Coaster Rider.\nYour ticket price is {ticket}")
    wants_photo=input("Do you want to have photos while riding roller coaster? Type y for YES or n for NO\n").lower()
    if wants_photo=="y":
        print(f"Your total price is {ticket+3}")
    else:
        print(f"Your total bill is {ticket}")    
    
else:
    print("SORRY! You cannot ride Roller Coaster")
''' 

##PIZZA ORDER
small=15
medium=20
large=25
total=0
size=input("what size pizza you want? S,M or L?\n").lower()


if size=="s":
    total=small
    pepperoni=input("Do you want pepperoni?\n")
    if pepperoni=="y":
        total+=2
    elif pepperoni !="n":
        print("Please enter Y or N")
        exit()
    extra_cheese=input("Do you want extra cheese?\n")
    if extra_cheese=="y":
        total+=1
       
    elif extra_cheese!="n":
        print("Please enter Y or N")
    print(f"Your total bill is {total}")
elif size=="m":
    total=medium
    pepperoni=input("Do you want pepperoni?\n")
    if pepperoni=="y":
        total+=3
    elif pepperoni !="n":
        print("Please enter Y or N")
        exit()
    extra_cheese=input("Do you want extra cheese?\n")
    if extra_cheese=="y":
        total+=1
        
    elif extra_cheese!="n":
        print("Please enter Y or N")
    print(f"Your total bill is {total}")
elif size=="l":
    total=large
    pepperoni=input("Do you want pepperoni?\n")
    if pepperoni=="y":
        total+=3
    elif pepperoni !="n":
        print("Please enter Y or N")
        exit()
    extra_cheese=input("Do you want extra cheese?\n")
    if extra_cheese=="y":
        total+=1
    elif extra_cheese!="n":
        print("Please enter Y or N")
    print(f"Your total bill is {total}")
else:
    print("Please Enter Correct Size")