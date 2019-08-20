def f(x):
    return x**2+1

def g(x, y):
    u = f(2**x)
    v = f(y**3)**0.5
    return (u+v)**(1/3)

a = 10
b1 = f(a)
b2 = f(2*a+1)
c1 = g(3, a)

print(a, b1, b2, c1)