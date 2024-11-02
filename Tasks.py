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
