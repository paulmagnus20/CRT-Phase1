tuple=("paul","Magnus","sahasra",1,2,3,4,3.14)
print(tuple)
print(type(tuple))
tuple=tuple+("hello",)
tuple=tuple+(13,23,"hello")
print(tuple)
for i in range(0,5):
    n=int(input("enter"))
    tuple=tuple+(n,)