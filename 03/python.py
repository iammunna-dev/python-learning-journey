#Finding the ODD or EVEN number and use of if else
'''
age=int(input("Enter your age: "))
odd_even= age%2
if odd_even==0:
    print("Your age number is EVEN")
else:
    print("Your age number is ODD")
'''

'''
weight = 85
height = 1.95

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

#USE of Nested and ELIF

print(f"Your BMI is: {bmi}")
if bmi<18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal Weight")
else:
    print("Overweight")
    
'''
'''
height=float(input("'Enter your height: \n"))
if height>120:
    age=float(input("Enter your age: \n"))
    if age<8:
        bill=5
        print("Ticket price is $5")
    elif age<15:
        bill=7
        print("Ticket price is $7")
    elif age<21:
        bill=10
        print("Ticket price is $10")
    elif age>=45 and age<=55:
        bill=0
        print("You will get free ticket")
    else:
        bill=12
        print("Ticket price is $12")
    photo=input("Do yo want to take photos? Type y for YES and n for NO: \n")
    if photo=="y":
        print(f"Your total bill is : ${bill+3}")
    else:
        print(f"Your Total Bill is: ${bill} Dollars")
else:
    print("Grow your height to enjoy the ride")

'''

