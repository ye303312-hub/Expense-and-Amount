expenses=[]
while True:
    name=input("enter expense name:")
    amount=float(input("enter amount:"))
    expenses.append(amount)
    answer= input("add another expense?(yes/no):")
    if answer=="no":
        break
print("total expenses:", sum(expenses))