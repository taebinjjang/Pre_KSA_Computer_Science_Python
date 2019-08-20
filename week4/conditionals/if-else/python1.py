def quadrant(x, y):
    if x == 0 or y == 0:
        print("on x-axis or y-axis")
        if x == 0 and y == 0:
            return "at origin"
        elif x == 0:
            return "on y-axis"
        else:
            return "on x-axis"
    else:
        print("on one of four quadrants")
        if x > 0 and y > 0:
            return "first quadrant"
        elif x < 0 and y > 0:
            return "second quadrant"
        elif x < 0 and y < 0:
            return "third quadrant"
        else:
            return "fourth quadrant"