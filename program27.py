u=input("Enter username: ")
p=input("Enter password: ")
for i in range(3):
    if u=="admin" and p=="1234":
        print("Login Success")
        break
    else:
        print("Login Failed")
        break

#Output
#Enter username: admin
#Enter password: 1234
#Login Success
