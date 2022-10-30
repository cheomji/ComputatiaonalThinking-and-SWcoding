#펭수의 망명
from stack import *

st = getstack()
output = []
cnt = 1

line = [int(item) for item in input().split()]
for item in line:
    push(st, item)
    output.append('S')
    for _ in range(len(st)):
        if top(st) == cnt:
            pop(st)
            output.append('X')
            cnt+=1
    

if not isEmpty(st):
    print('impossible')
else:
    for item in output:
        print(item, end='')
