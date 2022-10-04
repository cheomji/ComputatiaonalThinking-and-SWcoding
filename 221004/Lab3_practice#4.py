n = int(input('N=? '))
lst = []
black = []
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
for i in range(n):
    for j in range(i+1, n):
        if (lst[i][1] - lst[j][1])**2 + (lst[i][2] - lst[j][2])**2 < 4 :
            if lst[i][0] not in black:
                black.append(lst[i][0])
            elif lst[j][0] not in black:
                black.append(lst[j][0])
print("----Pengsu's Blacklist----")
for i in range(len(black)):
    print(black[i])
