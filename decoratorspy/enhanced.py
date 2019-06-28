#in python functions always return value
#by default it is none
#decoraters functions need keyword args


#HOW TO ACCOMODATE ARGUMENTS(*ARGS)
#HOW TO ACCOMODATE RETURN VALUES

import time

def my_decorator(func):
    def wrapper( *args, **kwargs): #args prints no arguments value
        t1 = time.time()
        rv = func(*args, **kwargs) #kwargs print named arguments
        t2 = time.time()
        print(f"TIME taken: {t2-t1}") #get time taken by functions to run and finish
        #return None #by default functions returns NONE
        return rv
    return wrapper


