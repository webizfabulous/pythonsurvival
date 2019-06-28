#how to use __str__?

class Point:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self): #this will be called automatically when we call a new object
        s= '('+ str(self.x) +','
        s+= str(self.y) + ')'
        return s



x = Point(1,2)
print(x.x) #calling x 
print(x) #the __str__ will be called automaticaally when we call object
#ouput:- (1,2)

