def mortage(cash):
    if cash>=50000:
        print("Instant Approval")
    elif cash>=2000 and cash<50000:
        print("Need appproval")

    else:
        print("Not Approved for mortage yet")
cash=int(input("Enter your cash: "))
Total_balance=0
while cash!=0:
    Total_balance+=cash
    mortage(cash)
    cash=int(input("Enter your cash: "))
print("total amount deposited: ",Total_balance)
