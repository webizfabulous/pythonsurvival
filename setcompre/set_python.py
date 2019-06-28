#A set looks like a mathematical set, usings curly braces

#{1,2,3,4} {'JOhn' ,'paul' , 123,'22'}

#you can asssign set to variable , just with any data
#you can add duplicated value in set but it ignores

a_set= {1,2,3,3,2,4 ,4}
#>>>a_set
#output: {1,2,3,4}
#>>> len(a_set)
#output:4

#order of elements of sets is not significant.
#order doesnt matter

b_set = {1,2,3}
c_set = {3,2,1}
b_set == c_set 
#output: True
b_set == {1,2,3,4}
#output :False


#sorting in set not supported , if u want to sort sets
#convert it to a list first then sort.

#a_set = {} #error this creates a dictionary

#instead use ,  a_set = set()

#add members by using add , a_set.add(1)

