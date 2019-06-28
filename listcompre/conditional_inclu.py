#include positive number only


#HARD WAY
num_list = [1,-1,2,-2,5,-7]

pos_list = []
for i in num_list:
    if i>0: #include positive numbers only
        pos_list.append(i) #append each positive number

print(pos_list)  #print [1,2,5]

#EASY WAY

#if, else in list comprehension
#syntax: [value+1 if value>0 else value+2 for value in range]
#it means add each value to 1 if the range value is greater than 0 else add each value to 2

#print all i which is greather than 0
hos_list = [i for i in num_list if i>0]
print(hos_list)

#advanced
#add 1 to i if i is greater than 0
#else add 2 to i
hos_list = [i+1 if i>0 else i+2 for i in num_list ]
print(hos_list)