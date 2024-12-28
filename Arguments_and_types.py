#Types of arguments
#1.positional argu
#2.default argu
#3.keyword argu
#4.variable argu
#5.variable length keyword argu

def power_of(a, b): #this is the positional argument
    c =a**b
    return c


power_of(5,2)

def power__of(a, b=2):#this is the default argument
    c=a**b
    return c
power__of(10) #we can also give two value in the argument example power__of(3,6)
              #note: You cannot give default value after any non default argument.

#key word argument and variable len argument
def power_of(a,b):
    c=a**b
    return c
power_of(b=2,a=4) #in key word argument position does'nt consider

#variable length arguments
def godown(*items): #one parameter only can print only one argument but some time a
                    #you need to print more then one then you should use * means len of total argument
    print(items)
godown("metal","iron","steel")

#another example 
def godown_items(name,*items,day):
    print(name)
    print(items)
    print(day)
godown_items("bro","steel","iron","metal",day="friday") #after len argument you should mention key value=value(insert_value)

#variable len argument
def college_data(**data):
    print(data)
    print(type(data))
college_data(name="bro",age=22,marks=99) #use ** to execute variable+key word argument passing 
                                         #note: * = len of variable ,** = variable + key word argu
    

    
