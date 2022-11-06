#lab6 assignment 그 감염 판별하는 문제

cnt = 0
n = int(input())
isInfected = [False for _ in range(n)]

for i in range(n):
    line = input()
    if len(line)<7 or line[:2] != 'AG' or line[-2:] != 'TC':
        continue
    for j in range(2, len(line)-4):
        if (line[j] == 'A'):
            check = line[j:j+3]
            if check == 'ATT':
                isInfected[i] = True
                break

for i in range(n):
    if isInfected[i] == True:
        cnt += 1
        print('Infected')
    else:
        print('Not infected')

print("Mission:", end=' ')
if (cnt/n >= 0.7):
    print("Possible")
else:
    print("Impossible")
