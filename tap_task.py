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
