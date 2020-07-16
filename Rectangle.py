'''
    Author: Leslie N. K
    Assignment 1
'''
#Point class to create coordinates of the rectangle
class Point:   
    def __init__(self,x,y):  #Function to set variables to their instances
        self.xcord = x
        self.ycord = y

    def move(self, x, y): #Function to move the Point around the coordinates
        self.xcord += x
        self.ycord += y

#Rectangle class
#With variables bottomLeft, topRight, length, and height
class rectangle:
    def __init__(self, bottomLeftCorner= Point(1,0), topRightCorner = Point(0,1)):
        self.bottomLeftCorner = bottomLeftCorner
        self.topRightCorner = topRightCorner
        self.length = bottomLeftCorner.ycord - topRightCorner.ycord
        self.width =  topRightCorner.xcord -bottomLeftCorner.xcord

    def perimeter(self): #Determines the perimeter
        return (2 * self.length) + (2 * self.width)

    def area(self):   #Determines the area
        return self.length*self.width


Rec1 = rectangle(Point(3,10),Point(4,8))# An object to create the rectangle
#Prints the results of the area and perimeter
print (Rec1.perimeter()) 
print (Rec1.area())
        
