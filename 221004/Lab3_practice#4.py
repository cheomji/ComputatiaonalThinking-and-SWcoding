n = int(input('N=? '))
lst = []
for i in range(n):
    tmp = []
    print('#', i+1, 'info (name, x, y)', sep='')
    line = input()
     #tmp 하지 말고 lst.append(line.split(',')[0], int(line.split(',')[1]), int(line.split(',')[2])) 이렇게 해도 됨
    name = line.split(',')[0]
    x = int(line.split(',')[1])
    y = int(line.split(',')[2])
    tmp.append(name)
    tmp.append(x)
    tmp.append(y)
    lst.append(tmp)
print(lst)
