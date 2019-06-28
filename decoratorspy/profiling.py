#decorates uses
#using decoraters in profiling
#decoraters helps in automation
#decorators helps to automate the functions


#we might want to see how slow  a function is if it calls print three times
import time

def print_msg():
    t1 = time.time()

    print('HI hello my name is not hree')
    print("Dexter is the greatest crimal show")
    print("Watch stranger things for adrneline rush")
    t2= time.time()
    print(f"function took , {t2-t1} times")


print_msg() 
#this is called profiling 
#profiling means getting time or statistics of a function
