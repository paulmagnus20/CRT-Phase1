def login():
    n=1
    while n!=0:
        uname_=input("Enter the Username")
        password=input("Enter the Password")
        if uname_==password:
            print("Successfully logged in")
            break
        else:
            print("incorrect")
login()