#The set type supportes a number of useful operations that closely parallel their mathematical equivalent.

#for example
a_set = {1,2,3,4,5,6,1,2,3}
b_set = {1,2,3,4,5}

#UNION
new_set = a_set.union(b_set) #also a|b
#output:{1,2,3,4,5,6}
print(new_set)


#INTERSECTION
new_set = a_set.intersection(b_set) #also a&b
#outputs commmon ..{1,2,3,4,5}
print(new_set)


#SET SUBTRACTION
#This last opeeration says
#GET EVERY MEMBER OF A_SET THAT IS NOT A MEMBER OF B_SET
new_set = a_set - b_set 
print(new_set)

