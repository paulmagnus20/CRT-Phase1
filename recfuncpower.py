def power(n,m):
    if m==0:
        return 1
    return n*power(n,m-1)
a=power(2,3)
print(a)