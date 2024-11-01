print("hello world)
#priting user name using f string
name = input("Enter Your Name :" )
print(f"Your Name is {name}")

#replacing the name using replace fucntion

#example 1
example1 = '''Dear Name ,You are selected!,Date'''
print(example1.replace("Dear Name", "Manu").replace("Date", "12/1/2023"))

#exmaple 2
example2 = "Hello Bro   My Name  is  Power Star"
print(example2.replace("  "," "))
      
#Finding a letter s and double space using "find" func
example3_fing_func = "HELLO BRO THIS IS  PYTHON"
print(example3_fing_func.find("  "))
