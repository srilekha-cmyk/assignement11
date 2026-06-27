amt=float(input("Enter amount: "))
if amt>=5000:
    print("20% Discount")
elif amt>=2000:
    print("10% Discount")
else:
    print("No Discount")

#Output
#Enter amount: 6000
#20% Discount
