# declare global variable
message = 'Hello world'

def greet():
    global message
    # local variable
    message = 'Hello' 
    print('Local', message)

# outside function 
def outer():
    message = 'local'
    # nested function  
    def inner():
        # declare nonlocal variable
        nonlocal message
        message = 'nonlocal'
        print("inner:", message)
    inner()
    print("outer:", message)

if __name__ == '__main__':
    outer()
    greet()
    # try to access message variable 
    # outside greet() function
    print(message)