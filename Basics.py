print("hello world)
#priting user name using f string
name = input("Enter Your Name :" )
print(f"Your Name is {name}")

#replacing the name using replace fucntion

#example 1
example = '''Dear Name ,You are selected!,Date'''
print(example.replace("Dear Name", "Manu").replace("Date", "12/1/2023"))

#exmaple 2
name = "Hello Bro   My Name  is  Power Star"
print(name.replace("  "," "))
      
#Finding a letter s and double space using "find" func
name = "HELLO BRO THIS IS  PYTHON"
print(name.find("  "))
