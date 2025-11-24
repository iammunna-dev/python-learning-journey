

'''

##TASK 1
value=int(input("Enter a Numeric Value:\n"))
if value<0:
    print(f"{value} is NEGATIVE")
elif value>0:
    print(f"{value} is POSITIVE")
else:
    print(f"{value} is ZERO")
if value%2==0:
    print(f"{value} is and EVEN Number")
else:
    print(f"{value} is an ODD Number")

    
#Task 2

value_one=int(input("Please enter first value:\n"))
value_two=int(input("Please enter second value:\n"))
operator=input("What you want to do? Please enter + or - or * or / :\n")
if operator=="+":
    print(value_one+value_two)
elif operator=="-":
    print(value_one-value_two)
elif operator=="*":
    print(value_one*value_two)
elif operator=="/":
    if value_two==0 or value_one==0:
        print("You cannot divide by ZERO(0)")
        exit()
    else:
        print(value_one/value_two)
else:
    print("Please enter correct operator")



#TASK 3
score=int(input("Please enter your score:\n"))
if score>=80 and score<=100:
    print("Your grade is A")
elif score>=70 and score<=79:
    print("Your grade is B")
elif score>=60 and score<=69:
    print("Your grade is C")
elif score>=50 and score<=59:
    print("Your grade is D")
elif score>=0 and score<50:
    print("Your grade is F")
else:
    print("Please enter your obtained score between 0-100")

#TASK 4

stored_username="iammunna"
stored_password="1122@0099"
username=input("Please enter your username\n")
password=input("Enter your passsword\n")
if stored_username==username and stored_password==password:
    print("Login Successful...")
else:
    print("Invalid username or password!")

    
    

#TASK 5
a=int(input("Enter first value:\n"))
b=int(input("Enter second value:\n"))
c=int(input("Enter third value:\n"))
if a>b and a>c:
    print(f"Largest value is {a}")
elif b>a and b>c:
    print(f"Largest value is {b}")
else:   
    print(f"Largest value is {c}")

    

#Task 6
print("Welcome to Celsius to Fahrenheit converter tool")
celsius=int(input("Enter temperature in Celsius:\n"))
to_fahrenheit= (celsius*(9/5))+32
print(f"{celsius} degree CELSIUS is {to_fahrenheit:.2f} degree in FAHRENHEIT")


#TASK 7 I made mistake on this and the answer below is copy pasted from chatgpt

year = int(input("Enter a year:\n"))

if year % 400 == 0:
    print(f"{year} is a LEAP YEAR")
elif year % 100 == 0:
    print(f"{year} is NOT a leap year")
elif year % 4 == 0:
    print(f"{year} is a LEAP YEAR")
else:
    print(f"{year} is NOT a leap year")

    '''
