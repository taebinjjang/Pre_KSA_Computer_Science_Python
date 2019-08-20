import math

a = math.sqrt(17)
b = math.sin(60 * math.pi / 180)
c = math.log(20 * b)

x1 = a + math.sqrt(c+1);
x2 = b * math.cos(x1) - 2;
d = math.cos(x2);

print(a, b, c, d)