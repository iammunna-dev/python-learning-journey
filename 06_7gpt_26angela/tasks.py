

'''
#Task1
list=[1,2,3,4,5,6,7,8,9]
new_list=[item for item in list if item%2==0]
print(new_list)

'''

#Task2
user_input=input("Write whatever you want:\n")
split_words=user_input.split()
print(split_words)
char_length=[(len(item)) for item in split_words]
print(char_length)

total_char= sum(char_length)
print(total_char)

##Task 3