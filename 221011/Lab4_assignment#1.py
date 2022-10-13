#integral
def func1(x):
    y = x**2
    return y

def func2(x):
    y = 1/x
    return y

def integral(f, a, b, N):
    total_area = 0
    h = (b-a)/N
    for i in range(N):
        x1 = a + i*h
        x2 = a + (i+1)*h
        total_area += h*(f(x1) + f(x2))/2
    return total_area

print(integral((func1), 0, 1, 10000))
print(integral((func2), 1, 2.71828182845904523536, 10000))
