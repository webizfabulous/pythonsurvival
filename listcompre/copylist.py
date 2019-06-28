#copying a list

k_list = [1,11,22,9,5]
#if we wann copy k_list 
j_list = k_list

#it will be copied but if we change a list

k_list.sort()

#j_list will also be sorted

print(k_list , j_list)

#TRUE COPYING
#old style
#one solution is to  use slicing , causing member-by-member copying.
a_list = [11,2,9,33,4]
b_list = a_list[:]
a_list.sort()

#b_list wont be sorted
print('After member copying' , a_list ,b_list)



#other solution
#using for loop
b_list = []
for i in a_list:
    b_list.append(i)

#you can also do variable
#like doubling or subtracting

list2 =[]
for in a_list:
    list2.append(i * 2)
#it wil append double