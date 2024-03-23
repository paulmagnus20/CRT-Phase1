class F15:
    def light(self):
        print("OK Switching on the lights")
    def fan(self,speed):
        print("Fan is on and the speed is:",speed)
        self.s=speed
    def cpu(self):
        print("The system is working")
        print(self.s)
class Shopping(F15):
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
Paul.fan(5)
Paul.cpu()
Paul.light()