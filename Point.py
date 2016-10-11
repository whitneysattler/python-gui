from math import *

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def distance(self, otherPoint):
        return sqrt((self.getX() - otherPoint.getX()) ** 2 + (self.getY() - otherPoint.getY()) ** 2)

    def isNearBy(self, p1):
        return (self.distance(p1) < 5)

    def __str__(self):
        return "(" + str(self.getX()) + "," + str(self.getY()) + ")"
    

    
