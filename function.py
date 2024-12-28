#There are 4types of functions
#1.user define function
#2.built in function
#3.Lambda function
#4.Recursion function

def cal():
    a = 22
    b = 10
    c = a*b
    print(c)
cal()

def cal(x, y):
    ans = x*y
    return ans # or print(ans)
cal(12,11)
    
def details(name, age):
    print(f"your name is{name}, and your age is{age}")
    
details("Bro",22)
