#Write a program to store seven fruits in a list entered by the user. 
fruits = []
user1 = input(str("Enter a fruit :"))
fruits.append(user1)
user2= input(str("Enter a fruit :"))
fruits.append(user2)
user3 = input(str("Enter a fruit :"))
fruits.append(user3)
user4= input(str("Enter a fruit :"))
fruits.append(user4)
user5 = input(str("Enter a fruit :"))
fruits.append(user5)
user6 = input(str("Enter a fruit :"))
fruits.append(user6)
user7 = input(str("Enter a fruit :"))
fruits.append(user7)
print(fruits)

#Write a program to accept marks of 6 students and display them in a sorted mannner.
students = []
st1 = int(input("Enter the marks student 1 :"))
students.append(st1)
st2 = int(input("Enter the marks student 2 :"))
students.append(st2)
st3 = int(input("Enter the marks student 3 :"))
students.append(st3)
st4 = int(input("Enter the marks student 4 :"))
students.append(st4)
st5 = int(input("Enter the marks student 5 :"))
students.append(st5)
st6 = int(input("Enter the marks student 6 :"))
students.append(st6)
students.sort()
print(students)

#Write a program to sum a list with 5 numbers
number_in_list = [10,30,50,60,80]
print(sum(number_in_list))

#Write a program, to count the numbet of zero in the follwing list.
numbers_in_list = [4,6,77,0,9,7,0,56,0,80,0]
find_zero = numbers_in_list.count(0)
print(find_zero)

#Write a program to create a dictionary of kannada words with values as their english translation. Provide user with an option to look it up!
dictionary = {"Namskara":"Hello","Dhanyavaad":"Thank you ","Vandanegalu":"Regards","Vidaya":"Bye"}
word = input("Entet the kannada word :")
print(dictionary[word])

#Write a program to input eight numbers from the user and display all the unique numbers (once).
num =set()
n = int(input("Enter a 1 numb :"))
num.add(n)
n = int(input("Enter a 2 numb :"))
num.add(n)
n = int(input("Enter a 3 numb :"))
num.add(n)
n = int(input("Enter a 4 numb :"))
num.add(n)
n = int(input("Enter a 5 numb :"))
num.add(n)
n = int(input("Enter a 6 numb :"))
num.add(n)
n = int(input("Enter a 7 numb :"))
num.add(n)
n = int(input("Enter a 8 numb :"))
num.add(n)
print(num)

#Create an empty dictionary allow 4 friends to enter their favourie language as values and keys will be their names. Then print each person's name along with their favourite language.
fav_lang = {}
a = input("Enter your friends names :")
b = input("Enter your languge :")
fav_lang.update({a:b})
a = input("Enter your friends names :")
b = input("Enter your languge :")
fav_lang.update({a:b})
a = input("Enter your friends names :")
b = input("Enter your languge :")
fav_lang.update({a:b})
a = input("Enter your friends names :")
b = input("Enter your languge :")
fav_lang.update({a:b}) 
print(fav_lang)

#Condition statement
#if,elif,else
#Write a program to print yes when the age entered by the user is greater than or equal to 18
if_elif_else_ = int(input("Enter Your Age :"))
if(if_elif_else_>=18):
  print("Yes")
else:
  print("No")

#Write a program to find the greatest of four number entered by the user.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))
if a>b and a>c and a>d:
  print(a,"is the greatest number")
elif b>a and b>c and b>d:
  print(b ,"the greatest number")
elif c>a and c>b and c>d:
  print("the greatest number is",c)
else:
  print("the greatest number is d")

#Write a program to find out wheather a student has passed or failed in an exam if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
marks1 = int(input("Enter marks of the first subject: "))
marks2 = int(input("Enter marks of the second subject: "))
marks3 = int(input("Enter marks of the third subject: "))
total_per = (100)*(marks1 + marks2 + marks3) / 300
if total_per >= 40 and marks1>33 and marks2>33 and marks3>33:
  print("You have passed the exam")
else:
  print("You failed")

#Write a program to find the given user name should contains 10 characters
user = input("Enter your name: ")
if(len(user))<=10:
  print("Your name characters are less than 10")
else:
  print("Your naem characters are more than 10")

#Write a program to find the given user name in the list
names_in_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
user = input(str("Enter a name : "))
if(user in names_in_list):
  print("Your Name In The List")
else:
  print("Your Name Not In The List")

#Write a program to caluclate the grade of a student from his marks from the following scheme:
#90-100=except
#80-90=A
#70-80=B
#60-70=C
#50-60=D
#<50=f

student = int(input("Enter Your Marks: "))
if student>=90 and student<=100:
  print("Your Grade is Excelent")
elif student>=80 and student<=90:
  print("Your Grade is A")
elif student>=70 and student<=80:
  print("Your Grade is B")
elif student>=60 and student<=70:
  print("Your Grade is C")
elif student>=50 and student<=60:
  print("Your Grade is D")
else:
  print("Your Grade is F")

#Tables
user = int(input("Enter a number :"))
for i in range(1,11):
  print(f"{i} X {i} = {user*i}")

#Finding a number is prime or not
n = int(input("Enter number"))
for i in range(2,n):
  if(n%i==0):
    print("The number is not prime")
    break
else:
    print("The number is prime")

#Finding a natural number of givin input

n = int(input("Enter the number :"))
i = 0
sum = 0
while(i<=n):
  sum = sum + i
  i = i+1
print(sum)

#Finding a greatest number of 3 variables using Def 
def func(a,b,c):
  if a>b and a>c:
    return a
  elif b>a and b>c:
    return b
  else:
    return c
print(func(1,2,3))


#Hacker Rank Problem
#To Find The Runner Up Score Given input
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(sorted(list(set(arr)))[-2])
  
#List Search Methode
sets = (1,4,9,4,0,3,66,934,33)
i = 0
user = int(input("Enter a number to seach for : "))
while i < len(sets):
  print(sets[i],end=" ")
  if user == sets[i]:
    print("Found it")
  else:
    print("Not found")
  i +=1

#table
user = int(input("Enter a number :"))
hod = 1
while hod <= 10:
  print(user,"x" ,hod,"=",user*hod)
  hod +=1  

#string finding in the given input
string = "m "
user = input(str("Enter Here :")).lower()
if string==user:
    print("no")
else:
    print("Yes")

#The given number is even or odd
user = int(input("Enter the number :"))
if user % 2 ==0:
    print("The number is even",user)
else:
    print("The number is odd",user)

#Wovles finding given user input
vowels = "aeiou"
count = 0
user = input("Enter a string :").lower()
for char in vowels:
    if char in user:
        count+=1
print(user)
print(count)

def gro():
  user_items=[]
  print("----WELCOME TO I GROCERIES----")
  items = {"milk":20,"bread":30,"eggs":70,"chicken":200,"apples":150}
  
  for i in items:
    print(i)
  while True:
    user = input("Enter your items: ").lower()
    print("Exit for press 4")
    if user == "4":
      break
    else:
      user_items.append(user)
  print(user_items)


gro()
