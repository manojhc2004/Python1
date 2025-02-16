#oops 

class human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def running(self):
        print(f"{self.name} is running and is age is {self.age}")

ninja = human("ninja",20)
ninja.running()
