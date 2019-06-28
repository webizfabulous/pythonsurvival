#lets focus on generators

#generator is special functions which yields one value at a time
#generator gives iterator
#we need syntax that generates one item at a time , then
#"yiels" a value , and waits to be called again, saving
#state information


#this is called generators a special case of iterator,
#We need a way to restart the iteration at the beginning
#whenever we need to (reusing the generator)

#we can use the iterator in any "for" statement
#we can also use the iterator with "in" and "not in " syntax


#iterator: an iterator is an object that can be looped upon.


#HOW GENERATORS WORKS?

#the "yield" keyword enables you to write a generator function

#we use generator when we dont wanna store all the values in the memory , which is really a generator factory

#yield means that it will output the value  , and save the state
#when we put yield in function , the functions becomes factory


#fatory means: it wont return value when we call a function , but a function address
#we cannot use generator from directly calling it
#use using next()

#EXAMPLE

def make_fibo_gen(n):
    a,b =0
    while a < n:
        yield a
        a , b = a+b ,a

my_gen = make_fibo_gen(1000)
print(next(my_gen))

#Generators save space in memory by computing values when they are needed,
#  instead of storing them in memory for use later.


