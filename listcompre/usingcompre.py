#now using list comprehension
#list comprehension is shortcut

#it consists of two pats within brackets [].
#the first part is the value to be produced ,for example ,i.
#second part of list comprehension is the for statement header.


# syntax : [value for_statement_header]

#example
old_list = [1,2,3]
#take each element from old_list and double it
new_list = [i*2 for i in old_list]
print(new_list)

#it is same like appending using for loop
"""
new_list = []

for i in old_list:
    new_list.append(i*2)
"""
#-->new_list = [i*2 for i in old_list]

