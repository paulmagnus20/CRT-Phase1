class Father:
    def __init__(self):
        print("Father= I am on time")
class Child(Father):
    def __init__(self):
        print("Child= I am Late")
obj=Child()