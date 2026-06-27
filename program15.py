s=float(input("Enter salary: "))
if s<250000:
    print("No Tax")
elif s<=500000:
    print("5% Tax")
elif s<=1000000:
    print("20% Tax")
else:
    print("30% Tax")

#Output
#Enter salary: 600000
#20% Tax
