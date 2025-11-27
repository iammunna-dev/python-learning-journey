import string

'''

val= string.ascii_lowercase
print(val)
val= string.ascii_lowercase[:3]
print(val)
val=string.printable
print(val)

'''
##Removing specific characters from a tring
email=" aleen\aha @gmail .com"
corrected_email= email.strip("")
print(corrected_email)

corrected_email= email.replace(" ","")
print(corrected_email)