m=int(input("Enter marks: "))
if m>=35:
    print("Pass")
    if m>=75:
        print("Distinction")
    elif m>=60:
        print("First Class")
else:
    print("Fail")

#Output
#Enter marks: 80
#Pass
#Distinction
