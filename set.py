set1={1,2,"Paul","kareem",3.14,True,False,"Suraj","Paul",4.13}
set2={2,3,"Suraj","Thanush",4.13,False}
print(set1)
print(set2)
set1.add("Karun")
print(set1)
set2.update("Mohana","Pragati","Siva")
print(set2)
set1.discard(True)
print(set1)
set2.remove("Suraj")
print(set2)
newset=set1.union(set2)
print(newset)
newset2=set1.intersection(set2)
print(set2)
newset3=set1.difference(set2)
print(newset3)
