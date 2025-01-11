#string is immutiable it can't change anything
name = "practice make man 'perfect'" #To highlighting a string or letter
print(name)

#string slicing
s = "guido van rossum"
print(s[0:6:2]) #[start:end:step]

#reverse slicing
s = "guido van rossum"
print(s[::-1]) #reversing a string

#negative slicing
s = "guido van rossum" 
print(s[-1:0:-1]) #negative slicing  -1 will change the direction

#concatenate the string using for loop
lst = ["bro","code","dude"]
string = ""
for i in lst:
  string = string + i + " "

print(string)

#join build in function
lst = ["bro","code","dude"]
string ="".join(lst)
print(string)

#startswitch and endswitch
lst = ["bro.com","dude.come","ninja.org"]
for i in lst:
  if i.endswith(".com"):
    print(i)
    
lsts = ["bro.com","dude.come","ninja.org"]
for i in lsts:
  if i.startswith("bro"):
    print(i)

#swap case build function
name = "bro DUDE"
name_swap = name.swapcase()
print(name_swap)

#formate method 
name = input("enter your name:")
place = input("enter your place:")
formate = "hello {},how is the weather in {}".format(name,place)
print(formate)

#formate function
s = input("enter your name").upper()
my_ans = "HELLO {} HOW ARE YOU {}".format(s,s)
print(my_ans)


#alignment using format function
s = "{:>5}".format("bro") #it will give the 5 spaces
print(s)
s1 = "{:$^}".format(150.00000) #left side = >
print(s1)              #right side = < , centre = ^ ,centre = ^

#printing the decimal points
import math
s ="{:.4f}".format(math.pi)#.no of decimal you need then F ,f means fixed notation

print(s)
