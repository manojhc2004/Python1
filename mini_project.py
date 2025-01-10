#small parking slot 
def parking():
  slots = {}
  slots_aval =10
  print("---WELCOME TO THE I5 PARKING SLOT---")
  while(len(slots)!=slots_aval):
    print("1.GET SLOT\n2.WHERE IS MY CAR\n3.EXIT")
    user = input("-ENTER YOUR CHOICE:")
    if user == "1":
      u1 = input("enter your name:").lower()
      u1_car = input("enter your car name:").lower()
      slots.update({u1:u1_car})
      print(f"your car slot is {len(slots)}")
    elif user == "" or " ":
      print("Invaild Enter!")
    elif user == "2":
      u2 = input("ENTER YOUR NAME:").lower()
      for name in slots.items():
        print(f"Your Car Slot is {len(name)}")
      if u2 == "" or " ":
        print("Invalid Enter!")
    else:
      if user == "3":
        print("Thank You For Using Our Services")
        break
      else:
        print("Invalid Enter")
  print("Slots Are Full!")


    
parking()

#print the given string is lower and upper and spceail character and store it in sperate
def string():
  lower,upper,special,number = 0,0,0,0
  user = input("Enter Your String :")
  for i in user:
    if i.islower():
      lower+=1
    elif i.isupper():
      upper+=1
    elif i.isnumeric():
      number+=1
    else:
      special+=1
      if user =="" or " ":
        print("Invalid Enter!")
  print(f"Lower case is :{lower}")
  print(f"Upper case is :{upper}")
  print(f"Special case is :{special}")
  print(f"Number case is :{number}")
