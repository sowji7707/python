import math
#local variable
def greet():
    message='hello'
    print(message)
greet()
#non local variable
num1=9
num2=10
sum=num1+num2
print(sum)
num1=10
num2=3
sum=num1+num2
print(sum)



#GLOBAL VARIABLE
c=1
def add():
    print(c)

add()

#global variable
# global variable
c = 1 

def add():

     # increment c by 2
    c = c + 2

    print(c)





#global variable
c=1
def add():
    global c
    c=c+2
    print(c)

add()

def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25
    
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)

outer_function()
print("Outside both function: ", num)

#python module addition
def add(a,b):
    result=a+b
    return result

import math
print(math.pi)
    
import math as m
print(m.pi)

from math import pi
print(pi)

from math import *
print(pi)
     


a = 1
b = "hello"

import math

dir()