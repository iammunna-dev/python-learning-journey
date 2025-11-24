

total_bill=float(input("Enter total bill amount: \n"))
tip = float(input("Enter how much(in percentage) tip you want to give: \n"))
bill_split=float(input("How many people to split the bill? \n"))
each_person_pay= (total_bill+(tip/100)*total_bill)/bill_split
print(f"Each person have to pay: {round(each_person_pay, 2)}")
