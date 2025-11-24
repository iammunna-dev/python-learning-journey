size=input("Choose the size of your pizza. S, M, L: \n")


price=0
if size=="s" or size=="m" or size=="l":
    pepporoni=input("Do you need pepporoni? y for YES and n for NO: \n")
    cheese=input("So you need exatra cheese? y for YES and n for NO: \n")
    if size=="s":
        price=15
    elif size=="m":
        price=25
    else:
        price=35
    if pepporoni=="y":
        if size=="s":
            price+=2
        elif size=="m":
            price+=3
        else:
            price+=4
    if cheese=="y":
        if size=="s":
            price+=3
        elif size=="m":
            price+=4
        else:
            price+=5
    print(f"Your Total Bill is: ${price}")
    
else:
    print("Please Enter Correct Size")