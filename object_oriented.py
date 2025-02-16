#oops 

class human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def running(self):
        print(f"{self.name} is running and is age is {self.age}")

ninja = human("ninja",20)
ninja.running()

class caluclator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def addition(self):
        res = self.num1 + self.num2
        print(f"the addtion is {res}")
    def subraction(self):
        res = self.num1 - self.num2
        print(f"the subraction is {res}")
    def multiflication(self):
        res = self.num1 * self.num2
        print(f"the multiflication is {res}")
    def divition(self):
        res = self.num1 / self.num2
        print(f"the divition is {res}")

num = caluclator(5 , 5)
num.addition()
num.subraction()
num.multiflication()
num.divition()
