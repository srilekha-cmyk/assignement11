u=int(input("Enter units: "))
if u<=100:
    bill=u*2
elif u<=200:
    bill=u*3
else:
    bill=u*5
print("Bill =",bill)

#Output
#Enter units: 150
#Bill = 450
