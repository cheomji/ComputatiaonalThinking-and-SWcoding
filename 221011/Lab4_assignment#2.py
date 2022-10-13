#몬테카를로 방식으로 원주율 계산
import random

n = int(input())
cnt = 0
for i in range(n):
    x = random.random()-0.5
    y = random.random()-0.5
    if x**2 + y**2 <= 0.5**2:
        cnt += 1
R = cnt / n
pi = R / (0.5**2)
print(pi)
