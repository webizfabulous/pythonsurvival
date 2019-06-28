#list comprehension and palindromes
#palindromes are words or sequence that reads the same backwards as forwards
#e.g madam , or nurses run
#integer: 121, 11211

#PALINDROMES WHAT IS?
#punctuation doesnt matter
#uppercase versus lowercase doesnt matter
#'Madam , I'm Adam' , 'A man , a plan , a canal , Panama!'


#HOW TO?

#start with a string.
# "A man  , a plan , a canal , Panama!"

#eleminate everything but alphabetic characters
#"AmanaplanacanalPanama"

#Convert to all lowercase and then test against its reverse
#"amanaplanacanalpanama"


#############################
#Using list comprehension will convert  a list of chars.
#include only chars that pass the test c.isalpha()
#the convert to lowercase with c.lower()
#list comprehension that performs all of this is:


#reverse syntax_list[::-1]
def is_pal(s):
    ls =[c.lower() for c in s if c.isalpha()]#for 'Racecar': ['r' , 'a', 'c','e','c','a','r']
    #isalpha() checks whether list consist of alphabet or not
    return ls == ls[::-1] # if list ls == reversed ls , reeturn true


print(is_pal("RAcecar"))
