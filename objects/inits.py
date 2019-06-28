#adding initialization (__init__)

#__init__ is special method
#method is a function defined inside the class

class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y



#the self identifier is must
#and if we wanna use x and y inside class
#we have to use self.x or self.y in other functions as well
#when pbject is called it will automatically call __INIT__ method
#self is the references to the object(POINT)
#self says im going to take these values and load


#this method definition enables us to
#Create point objects,in which each
#object has its own x and y.



#creating a object
#creates a copy of a object
pt1 = Point(1,2)
print(pt1.x , pt1.y) #pt1 is class and x and y is value we provided


