class cars:
    def _init_(self):
        self.cgst=1.8
        self.sgst=1.8
        self.insurance=100000
    def company(self):
        print("toyota","mercedes","rangerover")
        while True:
            self.n=input("enter a car company")
            if self.n=="toyota":
               print("select your model in:",self.n)
               self.model()
               break
            elif self.n=="mercedes":
                print("select your model in",self.n)
                self.model()
                break
            elif self.n=="rangerover":
                print("select your model in",self.n)
                self.model()
                break
            else:
                print("enter a correct company")
    def model(self):
        if self.n=="toyota":
            print("fortuner","land cruser")
            while True:
                self.model=input("enter the model")
                if self.model =="fortuner":
                    self.price(self.choice)
                    break
                elif self.model =="land cruser":
                    self.price(self.choice)
                    break
                else:
                    print("invalid")
        if self.n=="mercedes":
            print("g class","maybach")
            while True:
                self.model=input("enter the model")
                if self.model =="g class":
                    self.price(self.choice)
                    break
                elif self.model =="maybach":
                    self.price(self.choice)
                    break
                else: 
                    print("invalid")
        if self.n=="rangerover":
            print("svj","defender")
            while True:
                self.model=input("enter the model")
                if self.model =="svj":
                    self.price(self.choice)
                    break
                elif self.model =="defender":
                    self.price(self.choice)
                    break
    def price(self,choice):
        if choice=="fortuner":
            self.p=4500000
        elif choice=="landcruser":
            self.p==1000000
        elif choice=="g class":
            self.p=5000000
        elif choice=="maybach":
            self.p=60000000
        elif choice=="svj":
            self.p=7000000
        elif choice=="defender":
            self.p=9000000
        final_price=self.p + self.cgst + self.sgst + self.insurance
        print(final_price)
c=cars()
c.company()