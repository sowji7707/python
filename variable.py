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

#compound inst
#Find_value= P * (1 + r)^n
P=100000
r=0.07
n=10
r=pow((1+r),n)
print(type(P))
Find_value=P*r
print(Find_value)

