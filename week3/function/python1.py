import math

def distance(x1, y1, x2, y2):
    u = (x2-x1)**2
    v = (y2-y1)**2
    return math.sqrt(u+v)

def circleArea(radius):
    return math.pi * radius**2

def printCircleArea(radius):
    print(math.pi * radius**2)

if __name__=='__main__':
    a = circleArea(10)
    b = distance(0, 0, 3, 4)
    printCircleArea(10)
    print(a)
    print(b)