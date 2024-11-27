#1
user = 1111
user2 = 2222
def number(num):
    if num%10==0:
      return("yes")
    else:
         return("no")
print(number(user))
print(number(user2))

#2
num1 = 30
num2 = 40
if num1>num2:
    print(num1)
else:
    print(num2
#3
n1=10
n2=30
n3=57
n4=60
def number(n1,n2,n3,n4):
    if n1>n2 and n1>n3 and n1>n4:
        print(n1)
    elif n2>n1 and n2>n3 and n2>n4:
        print(n2)
    elif n3>n1 and n3>n2 and n3>n4:
        print(n3)
    else:
        print(n4)
number(n1,n2,n3,n4)
