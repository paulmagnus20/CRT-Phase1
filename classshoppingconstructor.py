class Shopping():
    def __init__(self,place):
        print("Welcome to Shopping at",place)
        self.place=place
    def DressType(self,dress):
        self.d=dress
    def Price(self,money):
        self.m=money
    def Size(self,size):
        self.s=size
    def Display(self):
        print(self.d)
        print(self.m)
        print(self.s)
        print(self.place)
Paul=Shopping("Peter England")
Paul.DressType("Peter England Shirt")
Paul.Price(5000)
Paul.Size("L")
Paul.Display()