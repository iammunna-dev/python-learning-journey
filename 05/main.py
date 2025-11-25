'''
#For loop
exam_scores=[80,90,95,83,77,72,85,93,97]
total=0
for scores in exam_scores:
    total+=scores
print(total)

#Finding sum without for loop

exam_scores=[80,90,95,83,77,72,85,93,97]
print(sum(exam_scores))



#Finding max using for loop
exam_scores=[80,90,95,83,100,72,85,93,97]
result=0
for maximum in exam_scores:
    if maximum>result:
        result=maximum
print(result)

#finding max without loop
exam_scores=[80,90,95,83,100,72,85,93,97]
print(max(exam_scores))


##Range function (1,10) does not include 10 and in default it increase by 1 but we can add custom increase number by (1,10,3) now it will increase by 3

#Sum of numbers in a range using for loops
total=0
for sum_of_numbers in range(1,101):
    total+=sum_of_numbers
print(total)

#Sum of numbers in a range without using loops
print(sum(range(1,101)))

##While Loop
num=10
while num>0:
    print(f"i love you {num}")
    num-=1

    '''