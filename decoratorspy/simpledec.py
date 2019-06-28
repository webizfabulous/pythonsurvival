#writing simple decorator
#decorator can be used to call many functions

#functions are objects which means that they can be argument to another functions


import time

def my_decorator(func):
    def wrapper(str):
        t1 = time.time()
        func(str) #exectute the original function
        t2 = time.time()
        print(f"time taken , {t2-t1}")
    return wrapper

def print_msg(str):
    print(str)

new_func = my_decorator(print_msg)
new_func('hello') #call wrapped function

#this can be written as

@my_decorator
def print_msg2(str):
    print(str)

print_msg2('hillo')