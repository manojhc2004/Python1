print("hello world)
#priting user name using f string
name_using_f_func = input("Enter Your Name :" )
print(f"Your Name is {name_using_f_func}")

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

#List sort
l1_list_sort = [1,3,4,5,6,7,8,9,10]
l1_list_sort.sort()
print(l1_list_sort)

#List reverse
l1_list_reverse = [1,3,5,7,9,39,40,50,60,70]
l1_list_reverse .reverse()
print(l1_list_reverse)
#append
l1_append = [1,3,4,7,8,9,10,55]
l1_append.append(60)
print(l1_append)

#Pop func
Poplistt_pop_func = [22,55,39,84,82,99]
listt_pop_func.pop(3)
print(listt_pop_func)
