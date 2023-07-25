print(10+3)
print(10-3)
print(10*3)

print(10/3)
#HERE WE GET FLOATING POINT NUMBER.

print(10//3)
#here we get integer.result=3

print(10%3)
#modulus operator.in this remainder is the result.

print(10**3)
#exponent or power operator

#incremented by 3
x=10
x+=3
print(x)

#decreased by 3
x=10
x-=3
print(x)

#OPERATOR PRECEDENCE

x=10+3*2
#3*2 executed first next add 10 to the result
print(x)

#THE ORDER OF THE OPERATOR PRECEDENCE
#EXPONENTIAL 2**3
#MULTIPLICATION OR DIVISION
#ADDITION OR SUBTRACTION

X=10 + 3 * 2 ** 2
#HERE FIRST OPERATION IS 2**2 NEXT 3*THE RESULT OF 2**2 NEXT ADDITION
print(X)

X=(10+3) *2 ** 2
#HERE FIRST OPERATION IS 10+3.NEXT 2**2.NEXT 13*4
print(X)

X=( 2 + 3) * 10 -3
#HERE FIRST OPERATION IS 2+3 NEXT 5*10 NEXT 50-3
print(X)

x=2.99
print(round(x))
#round function is bulit in function

print(abs(-2.9))
#ABS MEANS ABSOLUTE FUNCTION.BULIT IN FUNCTION.IT GIVES ONLY POSITIVE RESULT
