def isprime():
    f=1
    n=int(input("Enter the value:"))
    for i in range(2,n):
        if n%i==0:
            f=0
            break            
    if f==0:
        print("not prime")
    else:
        print("prime")
isprime()