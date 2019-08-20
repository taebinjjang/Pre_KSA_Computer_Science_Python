import math

def distance(x1, y1, x2, y2):
    u = (x2-x1)**2
    v = (y2-y1)**2
    return math.sqrt(u+v)

if __name__=='__main__':
    l = distance(0, 0, 3, 4)
    print(l)