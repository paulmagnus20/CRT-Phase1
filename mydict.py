mydict={
    120:"Paul",
    121:"Kareem",
    122:"Suraj",
    123:123,
    124:19,
    "124":190}
print(mydict)
mydict[103]="Thanush"
print(mydict)
print(mydict[121])
for i in mydict:
    print(i,end=" ")
for i in mydict.values():
    print(i,end=" ")
for i,j in mydict.items():
    print(i,j,end=" ")
mydict.pop(123)
print(mydict)