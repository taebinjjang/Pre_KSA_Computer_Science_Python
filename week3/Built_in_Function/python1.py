import math

a = math.sqrt(17)
b = math.sin(60*math.pi/180)
c = math.log(20*b)

d = math.cos(b * math.cos(a + math.sqrt(c+1)) - 2)

print(a, b, c, d)