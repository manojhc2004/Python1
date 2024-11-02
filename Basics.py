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
example3_find_func = "HELLO BRO THIS IS  PYTHON"
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
listt_pop_func = [22,55,39,84,82,99]
listt_pop_func.pop(3)
print(listt_pop_func)

#Remove func
litts_remove_func = [ 55,66,45,89,70,67,69]
litts_remove_func.remove(67)
print(litts_remove_func)

#Insert func
lits_of_insert_func = [44,33,22,56,76,89,78,90,34]
lits_of_insert_func.insert(5,100)
print(lits_of_insert_func)

#Class finding
what_class = (22,55,66,333,65)
print(type(what_class))

#Finding Index position 
finding_index_position_ = (22,55,66,333,65)
a_finding_index_position = finding_index_position_.index(55)
print(a_finding_index_position_)

#count the numbet of zero in the follwing list.
count_numbers_in_list = [4,6,77,0,9,7,0,56,0,80,0]
find_zero = count_numbers_in_list.count(0)
print(find_zero)

#dictionary
dictionary = {"sara": 50,"victor":60,"andy":70}
print(dictionary)

#in dictionary finding key and values#dictionary
dictionary_key_values = {"sara": 50,"victor":60,"andy":70}
print(dictionary_key_values.keys())
print(dictionary_key_values.values())

#dictionary get func
dictionary_get = {"sara": 50,"victor":60,"andy":70}
d_get_func= dictionary_get.get("sara")
print(d_get_func)

#sets
sets = {5,66,445,33,64,33,2}
sets.add(77)
print(sets)

#Condition statement
#if,elif,else
#Write a program to print yes when the age entered by the user is greater than or equal to 18
if_elif_else_ = int(input("Enter Your Age :"))
if(if_elif_else_>=18):
  print("Yes")
else:
  print("No")
      
#While loops
while_Loop = 1
while(while_Loop<6):
  print(while_Loop)
  while_Loop +=1
      
#for loops
for_loops =0
for x in range(10,101,5):
  print(x)

#for loop with else 
lists = ["manoj","anvi","anna"]
for i in lists:
  print(i,end=" ")
else:
  print("\nDone")
