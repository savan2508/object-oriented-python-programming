class Point:  

    def __init__(self,x,y):
        self.x = x
        self.y = y

# Uses the rectangular class to check for the 
    def falls_in_ractangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and \
        rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distance(self,x1,y1):
        dist = ((self.x-x1)**2+(self.y-y1)**2)**(1/2)
        return dist

class Rectangle:

    def __init__(self,lowleft,upright):
        self.lowleft = lowleft
        self.upright = upright

from random import randint

rectangle = Rectangle(Point(randint(0,9), randint(0,9)), \
    Point(randint(0,9), randint(0,9)))

print('Rectangle Coordinate: ','(',
      rectangle.lowleft.x,',',
      rectangle.lowleft.y,')','and',
      '(',rectangle.upright.x, ',',
      rectangle.upright.y,')')
        

