class Shopping():
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
Paul=Shopping()
Paul.DressType("Peter England Shirt")
Paul.Price(5000)
Paul.Size("L")
Paul.Display()