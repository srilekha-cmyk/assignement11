a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
if a+b>c and a+c>b and b+c>a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

#Output
#Enter first side: 3
#Enter second side: 4
#Enter third side: 5
#Valid Triangle
