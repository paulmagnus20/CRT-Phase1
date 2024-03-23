class F15:
    def light(self):
        print("OK Switching on the lights")
    def fan(self,speed):
        print("Fan is on and the speed is:",speed)
        self.s=speed
    def cpu(self):
        print("The system is working")
        print(self.s)
paul=F15()
paul.light()
paul.fan(5)
paul.cpu()