#에라토스테네스 어쩌구
n = int(input())

isPrime = [True for _ in range(n+1)]

# 0과 1은 소수가 아니다.
isPrime[0] = False
isPrime[1] = False

# 전략: isPrime이라는 리스트가 해당 index값이 소수이면 True, 아니면 False의 값을 가지도록 하고자 한다.
# 에라토스테네스 체의 원리 사용:
# (1)최근에 찾아낸 가장 작은 소수를 num이라고 지정.
# (2) 그리고 지정된 소수의 배수인 모든 index에 대해서 isPrime[i] 값을 False로 만든다.
# (3) 그 후, num보다 큰 index 중에서 가장 처음으로 isPrime[i] 값이 True인 숫자는 소수임이 자명하므로,
# (4) 다시 그 숫자를 num으로 지정한 후, 위의 2가지 단계(2~3)를 반복한다.

num = 2	# (1) 단계
while True:
	# (2) 단계
	for i in range(num+1, n+1):
		if i % num == 0:
			isPrime[i] = False
	# 위의 for문은 다음과 같이 더 효율적으로 구성이 가능하다!
	# (왜 그럴지에 대해서도 한 번 생각해보자..)
	# for i in range(num*2, n+1, num):
	#     isPrime[i] = False
	
	# (3) 단계
	for i in range(num+1, n+1):
		if isPrime[i]:
			num = i	# (4) 단계
			break
	
	# 종료 조건: 만약 현재 시점에서 더 이상 '소수일수도 있는'
	# 후보들이 존재하지 않을 경우 --> 종료! 
	# (후보: 아직 확실치는 않지만, isPrime[i] 값이 True인 index 값들)
	cnt = 0
	for i in range(num+1, n+1):
		if isPrime[i]:
			cnt += 1
			break
	
	if cnt == 0:
		break

for i in range(1, n+1):
	if isPrime[i]:
		print(i, end= ' ')
print()
