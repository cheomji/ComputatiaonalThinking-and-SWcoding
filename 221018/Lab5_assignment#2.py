#제곱수 분해 문제
def divide(prev):
    if sum(lst) == n:
        print('=', end=' ')
        for i in range(len(lst)-1):
            print(lst[i], '+', end=' ')
        print(lst[-1])
        return

    for i in range(prev, len(square)):
        if sum(lst) + square[i] <= n:
            lst.append(square[i])
            divide(i)
            lst.pop()

n = int(input('n: '))
square = [i*i for i in range(5, 0, -1)]
lst = []
divide(0)
