#creating a set using range

big_set =set(range(2,100)) #if we dont use set , list here it wont create anything

print(big_set)

#set comprehension works just like list comprehension
#with both list and set comprehension, we can do nested loop

#new_set => {value for_header_1 for_header_2}

comp_set = {j for i in range(2,100) for j in range(i*i , 100,i)}
print(comp_set)

#same like

comp_set = set()
for i in range(2,n):
    for j in range(i*i , n,i):
        comp_set.add(j)

