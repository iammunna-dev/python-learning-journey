import random #First import module to use randomisation
'''
int_number= random.randint(1000,9999)
float_number=random.random() #This random will generate a floating number that will be,  0<NUMBER<1
float_number_uniform=random.uniform(1000,9999) #This uniform will generate a floating number based on the value we put into the parentheses, 0<=NUMBER<=10
print(
    int_number,"\n",
    float_number,"\n",
    float_number_uniform
)

random_num=random.randint(0,1)
print(random_num)

'''

#Python LISTS and Related things

cities_of_bangladesh= ["Dhaka","Chittagong","Rajshahi","Barishal","Khulna","Rangpur","Mymensingh","Sylhet"]
cities_of_bangladesh.append("Comilla") #This adds single value to the end of the list
cities_of_bangladesh.extend(["Gazipur","Narayanganj"]) #This adds multiple values to the end of the list
cities_of_bangladesh.insert(0,"Kurigram") #This adds single value in a specifit position

print(cities_of_bangladesh[5])
print(cities_of_bangladesh)


