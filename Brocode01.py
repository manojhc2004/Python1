a=input("do you want to see district in karnataka,yes,no")
karnataka = ["Hassan","bengaluru","mysuru","kolara","mangaluru"]
if a=="yes":
    print(karnataka)
else:
    print("thank you")
   
b =input("do want to see what are famouse and best places in karnataka state\n,please seclet below distics,hassan,bengaluru,mysuru,kolara,mangaluru")
if b=="Hassan":
    print("Hassan is rich history,ancient architecture ,and antural beauty.")
elif b=="bengaluru":
    print("bengaluru is the nation's leadinh information technology(IT)exporter.")
elif b=="mysuru":
    print("mysuru is the historical places in mysuru are a peek into the glorious past of the city.")
elif b=="kolara":
    print("kolara is production milk and mining of gold.")
elif b=="mangaluru":
    print("mangaluru is a ancient 10th century Mangala Devi temple.")
else:
    print("please entre a above distics") 
  #2nd programm
    
print("THE GANGSTAS ESPORTS PLAYERS AND ROLES")
a = input("Do you see,Yes,No")
if a=="Yes":
    print("Devil,Igl,Valtxd,Neyo")
else:
    print("THANK YOU")
b = input("Do you want to see the roles of players,\nYes,No")
if b=="yes":
    print("Devil,Igl,Valtxd,Neyo, ")
else:
    print("THANK YOU")
c =input("PLEASE TYPE A NAME PLAYER,\nDevil,IGL,Valtxd,Neyo")
if c=="Devil":
    print("He is IGL and Enrty fragg")
elif c=="IGL":
    print("He is IGL and free man")
elif c=="Valtxd":
    print("He is Entry fragger")
elif c=="Neyo":
    print("He is also entrt fragg")
else:
    ("invaild player name please enter a vaild player")

#finding max number
number = int(input("ENTER A FIRST NUMBER"))
number1 = int(input("ENTER A SECOND NUMBER"))
number02 = int(input("ENTER A THIRD NUMBER"))
if number1<number and number02<number:
    print("max is",{number})
elif number<number1 and number02<number1:
    print("max is",{number1})
elif number<number02 and number1<number02:
    print("max is ",{number02})

#number guessing game:
secret_code =77
guess = int(input("ENTER A NUMBER TO FIND SECRET NUMBER  >>>"))
if guess==secret_code:
  print("You guessed it right")
elif guess<secret_code:
  print("you guessed it to low")
elif guess>secret_code:
  print("you guessed it too high")
else:
  print("invalid input")

# simple caluculator
print("this is a simple calculator")
user = input("ENTER A OPERATER,+,-,*,/:")
num01 = int(input("ENTER A FIRST 1ST NUMBER :"))
num02 = int(input("ENTER A SECOND 2ND NUMBER :"))
if user=="+":
  print(num01+num02)
elif user=="-":
  print(num01-num02)
elif user=="*":
  print(num01*num02)
elif user=="/":
  print(num01/num02)
else:
  print("invalid input",{num01,num02,user})

# FORM DETAILS 
print("FILL YOUR DETAILS AND SIGHN UP")
name=input("ENTER YOUR NAME :")
age=input("ENTER YOUR AGE :")
gender=input("ENTER YOUR GENDER,MALE,FEMALE :")
if age<=18:
  print("YOU ARE NOT ELIGIBLE FOR TO SIGN UP")
else:
  print("YOU ARE ELIGIBLE FOR TO SIGN UP")
print("YOUR DETAILS ARE HERE,YOUR NAME IS {name},YOUR AGE IS ,{age},GENDER,{gender}")


# tables:
usr = int(input("enter a number :"))
for i in range(1,11):
  print(f" {usr}, X {i} = {usr*i}")

#ATM MACHINE
user_pin = int(input("PLEASE ENTER AGAIN PIN CODE >>>> :"))
user_cash = 100000
print("CREADIT OR DEPOSITE,C/D")
user_choice = input("PLEASE ENTER ,CREADIT/DEPOSITE :")
if user_choice=="CREADIT":
  print("PLEASE ENTER AMOUNT/CASH BELOW")
  amount = int(input("ENTER NUMBER :"))
  print("PLEASE WAIT FOR YOUR TRANSATION")
  c_finall = user_cash-amount
  print("YOUR BALACE IS",c_finall)
  if user_choice=="DEPOSITE":
    print("PLEASE ENTER DEPOSITE AMOUNT BELOW")
    d_amount = int(input("ENTER HERE"))
    d_finall = user_cash+d_amount
    print(f"YOUR BALANCE IS {d_finall}")
  else:
    print("YOU ARE ENTERED WRONG ")
else:
  print("YOU ARE ENTERED WRONG")
    
#ATM MACHINE WITH DRAW ONLY
print("WELCOME TO THE ATM")
user_pinis = 776080
user_balance = (100000)
use = int(input("ENTER A PIN :"))
if use == user_pinis:
  print("<<<PIN IS CORRECT>>>")
else:
  print("YOUR PIN IS INCORRECT") 
home_page = input("PLEASE ENTER FROM THE FOLLOWING OPTIONS >>>,WITHDRAW, DEPOSIT ,BAL ")
if home_page == "WITHDRAW":
  us=input("YOU ARE SELECTED WITH DRAW,YES :")
  if us == "YES":
    w_d = int(input("ENTER A AMOUNT TO WITH DRAW :")) 
    cal = user_balance - w_d
    print("<<YOUR AMOUNT SUCCESSFULLY WITH DRAW YOUR BALANCE IS>>",cal)
  else:
    print("INVAILED")
else:
  print("INVALIED") 
    
#sorting number
numbers =144,33,22,65,78,92,101
2 numbers_sort = (sorted (numbers) )
print(numbers_sort)
             
        



  
