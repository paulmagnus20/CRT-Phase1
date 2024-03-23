list=[42,36,28,96,4,-1,1]
sum1=0
min=999
max=-999
for i in range(0,len(list)):
    if list[i]<min:
        min=list[i]
print(min)
for i in range(0,len(list)):
    if list[i]>max:
        max=list[i]
print(max)
sum1=max+min
print("Sum of min and max is:",sum1)