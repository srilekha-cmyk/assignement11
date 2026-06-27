a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
l=max(a,b,c)
if l==a:
    print(max(b,c))
elif l==b:
    print(max(a,c))
else:
    print(max(a,b))

#Output
#Enter first number: 10
#Enter second number: 30
#Enter third number: 20
#20
