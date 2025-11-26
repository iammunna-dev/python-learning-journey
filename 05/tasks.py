

'''
##TASK 1
for char in range(1,101):
    print(char)

##TASK 2
value=10
while value<=10 and value!=0:
    print(value)
    value-=1

##TASK 3
for i in range(1,51):
    if i%2==0:
        print(i)

##TASK 4
value=1
for i in range(1,12,2): #USING FOR LOOP
    print("*"*i)

while value<=5: ##USING WHILE LOOP
    print("*"*value)
    value+=1

##TASK 5
for i in range(1,6):
    for num in range(1,i+1):
        print(num,end="")
    print()


##FINDING FACTORIAL (was not in the task)
user=int(input("Enter a number:\n"))

fact=1
for i in range(1,user+1): ##USING FOR LOOP
    fact*=i
    
print(fact)

i=1
fact=1
while i<=user: ##USING WHILE LOOP
     fact*=i
     i+=1
print(fact)

#TASK 6
user=int(input("Enter a number:\n"))
for i in range(1,user+1):
    print(i,end=" ")

    #TASK 7
user=int(input("Enter a number:\n"))
for i in range(1,11):
    print(f"{user} * {i} = {user*i}")


'''


