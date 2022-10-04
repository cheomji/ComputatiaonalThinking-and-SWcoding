#랜덤묘듈 사용하기
import random
a = []
for i in range(6):
    num = random.randint(1, 45)
    while num in a:
        num = random.randint(1, 45)
    a.append(num)
print(a)

#어펜드 대신 인서트에 해도 상관 없ㅇㅇ. 그리고 randint 말고 randrange(1, 46) 써도 됨
