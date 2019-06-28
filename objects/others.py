#using other method


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        s = '(' + str(self.x) + ','
        s+=str(self.y) + ')'
        return s

    def dist(self , other):
        dx = self.x - other.x
        dy =self.y - other.y
        return (dx * dy * +dy * dy ) ** 0.5


#asumme class definition in place
#the call will be pt1.dist(p2)
#Do the following

pt1 = Point(1,2)
pt2 = Point(10,5)
print(f'Dist betweem {pt1} and {pt2} is {pt1.dist(pt2)}')
