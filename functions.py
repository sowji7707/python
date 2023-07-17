'''
functions:
 repetable task:

 inputs: they are called arguments (optional) 
 outpus: None or else you can specify 

 in-built functions: len(my_list), sum(my_list), print("message")


'''

def greet(msg):
    print(msg)


greet("hello world")
greet("hello world2")


def square_list(my_list):
    out_list = []
    for item in my_list:
        out_list.append(item**2)
    return out_list

def check_leap_year(num):
    if num%4==0:
        print(f"{num} is a leap year")
    else:
        print(f"{num} is not a leap year")
    # return None

# function with two arguments
def add_numbers(num1=5, num2=2):
    sum = num1 + num2
    print('Sum: ',sum)

in_list = [1,2,3,4,5]

list_out = square_list(in_list)
print(list_out)
list_out2 = square_list([1,2,3,5])
print(list_out2)
check_leap_year(3956)
check_leap_year(3946)

# function call with two values
add_numbers(5, 4)
add_numbers(5, 10)
add_numbers()