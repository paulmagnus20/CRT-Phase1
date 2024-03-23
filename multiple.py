class F15:
    def light(self):
        print("OK Switching on the lights")
    def fan(self,speed):
        print("Fan is on and the speed is:",speed)
        self.s=speed
    def cpu(self):
        print("The system is working")
class Shopping:
    def DressType(self,dress):
        self.d=dress
        print(self.d)
    def Price(self,money):
        self.m=money
        print(self.m)
    def Size(self,size):
        self.s=size
        print(self.s)
class shop(F15,Shopping):
    def k(self):
        print("ShopName")
paul=shop()
paul.k()
paul.Price(5000)
paul.cpu()
