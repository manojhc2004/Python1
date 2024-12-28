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
    

    
