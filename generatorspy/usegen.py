#how to actually use generator

#we can use loop to call generator

#TWO KINDS OF GENERATOR

#generator for finite object to yield



#Generator for infinite
#if infinite called then the for loop will also be infinite


def make_sqr_gen():
    yield 5 #it would be called once
    i=n=1 #let i and n is 1
    while True: #till true
        i+=2 #add 2 to i
        n+=i #add i to n
        yield n #give n
       # if n>10: #if n is greater than 10
        #    return False #return false end the loop


x = make_sqr_gen()
for y in x:
    if y >100:
        break
    print(y)

