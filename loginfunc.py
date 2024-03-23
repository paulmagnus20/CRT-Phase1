def login():
    uname_=input("Enter the Username")
    password=input("Enter the Password")
    if uname_==password:
        print("Successfully logged in")
    else:
        print("incorrect")
        login()
login()
    