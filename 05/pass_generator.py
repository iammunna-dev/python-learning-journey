##RANDOM PASSWORD GENERATOR

import random

'''

letter=["A", "a", "B", "b", "c", "C", "D", "d", "E", "e", "F", "f", "G", "g", "H" , "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n"]
number=[0,1,2,3,4,5,6,7,8,9]
symbol=["!","@","#","$","%","&","*","(",")","-","+","/","?","~"]

user_number=int(input("How many number in your password you want?"))
user_letter=int(input("How many letter in your password you want?"))
user_symbol=int(input("How many symbol in your password you want?"))

rand_number=(random.choices(number, k=user_number))
rand_letter=(random.choices(letter,k=user_letter))
rand_symbol=(random.choices(symbol,k=user_symbol))

password=rand_letter+rand_number+rand_symbol
random.shuffle(password)
password="".join(str(x) for x in password)   ### If we had stored the numbers as strings, then we would not need to use the str(x) and for loop here to convert the whole password in string. We could have just write password="".join(password) instead.

print(password)

'''


###PASSWORD GENERATOR WITHOUT ANY SPECIFIC USE LIMIT ON THE LETTER,NUMBER ANF SYMBOL

digits=["A", "a", "B", "b", "c", "C", "D", "d", "E", "e", "F", "f", "G", "g", "H" , "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n","!","@","#","$","%","&","*","(",")","-","+","/","?","~","1","2","3","4","5","6","7","8","9"]

user_number=int(input("How many digits you want in your password? :\n"))

password= "".join(random.choices(digits, k=user_number))

print(password)


