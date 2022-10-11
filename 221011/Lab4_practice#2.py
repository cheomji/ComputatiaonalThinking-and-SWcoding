def firstNEnenFibonacciNumbers(n):
    fibo = []
    lst = [1,1]
    cnt = 0
    while cnt != n:
        if (lst[-1] + lst[-2])%2 == 0:
            cnt += 1
            fibo.append(lst[-1] + lst[-2])
        lst.append(lst[-1] + lst[-2])
    return fibo

print('firstNEnenFibonacciNumbers(5):', firstNEnenFibonacciNumbers(5))

#you can use index such as '-1' or '-2'
