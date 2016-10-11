class Rectangle2D:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def getArea(self):
        return self.__height * self.__width

    def getPerimeter(self):
        return 2 * (self.__height + self.__width)

    def containsPoint(self, x, y):
        xDist = abs(x - self.__x)
        yDist = abs(y - self.__y)
        return ((xDist < self.__width / 2) and (yDist < self.__height / 2))

    def containsRectangle(self, rectangle):
        lBound = rectangle.getX() - rectangle.getWidth() / 2
        rBound = rectangle.getX() + rectangle.getWidth() / 2
        uBound = rectangle.getY() - rectangle.getHeight() / 2
        dBound = rectangle.getY() + rectangle.getHeight() / 2
        return self.containsPoint(lBound, uBound) and self.containsPoint(rBound, dBound)

    def overlaps(self, rectangle):
        xDist = abs(self.__x - rectangle.getX())
        yDist = abs(self.__y - rectangle.getY())
        return xDist < (self.__width + rectangle.getWidth())/2 and yDist < (self.__height + rectangle.getHeight())/2

    def __contains__(self, another):
        return another.containsRectangle(self)

    def __cmp__(self, another):
        temp = self.getArea() - another.getArea()
        if temp > 0:
            return 1
        elif temp < 0:
            return -1
        else:
            return 0

    def __lt__(self, another):
        return self.getArea() < another.getArea()

    def __le__(self, another):
        return self.getArea() <= another.getArea()

    def __eq__(self, another):
        return self.getArea() == another.getArea()

    def __ne__(self, another):
        return self.getArea() != another.getArea()

    def __gt__(self, another):
        return self.getArea() > another.getArea()

    def __ge__(self, another):
        return self.getArea() >= another.getArea()
