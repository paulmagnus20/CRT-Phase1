list1=[1,2,"Paul","Pragati",3.14]
list1.append("college")
list1.insert(3,"ece")
print(list1)
for i in range(0,len(list1)):
    print(list1[i])
for i in list1:
    print(i)
print(list1[0])
print(list1[2:5])
print(list1[:5])
print(list1[-1:])
print(list1[::-1])
list1[3]="Aditya"
print(list1)