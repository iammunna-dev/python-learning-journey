import string

a = [1,2,3]
b = a  # both point to same list but not recommended
print(b)

##Right way of copying list
b=a.copy()
print(b)

##slicing
b=a[:2]
print(b)

##ADDING ITEMS
a.append(4) #add ONE item
print(a)

a.extend(["A",5]) #add multiple items
print(a)

a.insert(1,"Hey") #add item at specific index
print(a)


