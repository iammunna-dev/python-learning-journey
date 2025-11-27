##LIST COMPREHENSION

'''
##NORMAL METHOD
list=[1,2,3,4,5]
new_list=[]
for n in list:
    new_list.append(n+1)
print(new_list)


##LIST COMPREHENSION METHOD
list=[1,2,3,4,5]

new_list=[items+1 for items in list]
print(new_list)

name="munna"
new_list=[item for item in name]
print(new_list)

list=[item*2 for item in range(1,6)]
print(list)

list=["Alex","Eleanor","Hrodger","Djoser","Roma","Yakup","Ade", "Ibrahim"]
new_list=[item.upper() for item in list if len(item)>=5]
print(new_list)

'''
