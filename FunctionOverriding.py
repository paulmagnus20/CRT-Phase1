class Father:
    def bike(self):
        print("Harley Davidson")
    def laptop(self):
        print("Laptop with 2GB")
class Me(Father):
    def laptop(self):
        print("As per my requirements")
        print("Laptop with 8GB")
obj=Me()
obj.bike()
obj.laptop()