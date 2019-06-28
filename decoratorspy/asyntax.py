#functions are objects in python
#functions are first class objects in python
#we can use any valid  name to label a function

new = my_decorator(print_stats)


#we can also name original name of the function

print_stats = my_decorator(print_stats)

#decoraters wraps code around it

#decorators helps to reuse the functions with another function
#by using @

#@decorator_name
#function_defination

@decorator
def func():
    pass

#this translates to
#function_defination
#function_name = decorator_name(function_name)
func = decorator(func)

#Perhaps not surprisingly, you can apply more than one decorator to a function.


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return 'hello!'

greet()

#output :- '<strong><em>Hello!</em></strong>'