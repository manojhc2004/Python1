#slicing 
my_list = [ 1,3,2,5,56,"no"]
print(my_list)
print(my_list[1:6])
print(my_list[-5])
print(my_list[::-1])
print(my_list[1:5:2])

#append function
students = [55,89,76,65,93,50,72]
high_score = []
for high in students:
    if high>=70:
        high_score.append(high)
   
print(high_score)

#sum function
num = [ 1,3,5,7,9,2]
sum_num = sum(num[:4])
print(sum_num)
slise = num[4:]
print(slise)

#methods in list
#len
my_list =[12,3,4,665,32,2,9]
print(len(my_list))

#changing elements
my_list = [2,5,7,3,1]
my_list[1]=10
print(my_list)

#change a range of item values
my_list = [2,5,7,3,1,4,8]
print(my_list)
my_list[1:3] = [20,40]
print(my_list)

#add list items
my_list =[2, 20, 40, 3, 1, 4, 8]
my_list.append(20)
print(my_list)

#join two list
list1 = [2, 20, 40, 3, 1, 4, 8]
list2 = [2, 10, 7, 3, 1]
add = (list1 + list2)
print(add)

#checking the element
my_list = [2, 20, 40, 3, 1, 4, 8]
find = 3 in my_list
print(find)

#reverse method in list
my_list = [2, 20, 40, 3, 1, 4, 8]
cut = my_list[2:5]
cut.reverse()
print(cut)

#calculate the average score for each section
classA = [85,90,88,92,78]
classB = [75,82,80,85,79]

classA_avg = sum(classA)/len(classA)
classB_avg = sum(classB)/len(classB)
print("Class A Students Average is",classA_avg)
print("Class B Students Average is",classB_avg)


#practice questions
#my_list = [10,20,30,40,50]
#a.add the value 60 to the end of the list 
#b.insert the value 5 at the beginning of the list
#c.remove the value 30 fromt the list
#e.print the modified list

my_list = [10,20,30,40,50]
my_list.append(60)
my_list[0] = 5 #or my_list.insert(0,5)
my_list.pop(2) #or my_list.remove(30)
print("Modified List",my_list)

#Practice question
#take a number of persons 
#take a persons age and insert in list
#Seprate the child,adults and seniors

no_of_persons = int(input("enter the of no persons :"))
all_ages = []
diff_age = []
for i in range(no_of_persons):
    ages = int(input("Enter Your Age :"))
    all_ages.append(ages)
child = 0
adults = 0
senior = 0
for dif_ages in all_ages:
    if dif_ages<=18:
        child = child +1
    elif 18 < dif_ages <=65:
        adults = adults +1
    else:
        senior = senior +1
print("No of Childerns ",child)
print("No of Adults ",adults)
print("No of Seniors",senior)
