#Object Oriented Programming!!!! >:)
from math import * #Bad practice using import *

class Point:
    def __init__(self, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord
    def distanceToPoint(self, point2):
        return sqrt((self.x - point2.x)**2 + (self.y - point2.y)**2)
    def magnitude(self):
        origin = Point(0,0)
        return self.distanceToPoint(origin)

def main():
    a = Point(4, 6)
    b = Point(1, 2)

    dist = sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


    print("The distance between the points is:", dist)



main()