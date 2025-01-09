#printing the all substring
user = input("enter a string:")
for i in range(0,len(user)-2):
    print(user[i:i+3])

#printing the string ignoring the first character ans last character
user = input("enter a string:")
for i in range(1,len(user)-1):
  print(user[i])
    #or
ans = user[1:-1]
print(ans)

#printing the string in reverse order ans ignoring the last character and first character
user = input("enter a string:")
ans = user[-2:0:-1]
print(ans)

#check the given string is palindrome or not
def string(name):
    front=name[0:] #manoj
    rev=name[::-1] #jonam
    if front == rev:#manoj==jonam  is not palindrome
        print(f"The given string is palindrome",name)
    else:
      print(f"The given string is not a palindrome",name)
print(string("manoj"))

#checking the two strings are equal or not
s1= "python"
s2 = "JAVA"
if s1 == s2:
    print("equal")
else:
    print("not equal")

#cut the mid value of the string starting to mid ,and reverse the mid value +characters
s1 = "nan"
mid = s1[:len(s1)//2:]
rev = s1[len(s1)-1:(len(s1)//2)-1:-1]
ans = mid+rev
print(ans)

#check the two string are equal or not with ignoring the case sensitive
s1 =input("enter a first string:")
s2 = input("enter a second string")
if s1.lower() == s2.lower():
    print("equal")
else:
    print("not equal")

