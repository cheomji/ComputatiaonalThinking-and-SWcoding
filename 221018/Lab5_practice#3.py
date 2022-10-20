#교수님코드.. 인데 이게 뭔개소리죠?ㅋㅋ

# Practice #3: 대도 펭수 문제 풀이

# 발자국 패턴을 다채롭게 남기는 것이 핵심!
# 우리가 배웠던 4가지 패턴 -> 중복을 {허용,허용하지 않는} {순열, 조합} 중 어떤 방식을 적용해야 할지 고민하여 봅시다!
# 결론) 중복을 허용하는 순열 문제! 단, 아래와 같은 추가 조건들을 고려해야 한다.


# 따져봐야 할 세부 조건:
# (1) 연속으로 같은 거리 만큼을 움직이는 경우 -> 금지!
# 	예) 30 30 50    혹은   50 50 70
#   해결책) 직전에 이동한 거리를 prev와 같은 변수로 전달 받아서, 다음 step은 그 거리 만큼을 움직이지 않는 쪽으로!
# (2) 두 종류의 보폭이 반복되는 경우 -> 금지!
#   예) 30 50 30 50 70		혹은		50 70 50 70 30
#	해결책) 아래의 check() 함수를 통해서 검증하여 본다 --> 현재까지의 step에 대한 정보를 담고 있는 리스트를 바탕으로 비교한다.
#		    footprint 리스트에 대해서 [-3], [-2], [-1]번째 index에 위치한 step 값을 비교한다 -> [-3]과 [-1]의 값이 같고, [-2]번째 값과 현재 선택하려는 i번째 크기[30,50,70 중 i번째] 값과 같으면 피해야 하는 패턴!

# 다음과 같은 경우는 가능하다: 30 50 70 30  혹은 30 50 30 70

# (2)번 조건을 위한 함수
def check(footprint, currentStep):
	if len(footprint) < 3:
		return False
	return (footprint[-1] == footprint[-3]) and (footprint[-2] == dist[currentStep])

def pengsu(steps, prev, footprint):
	# (1) Base case: 발 걸음 수가 n 발자국을 넘어서면 추가적인 재귀호출 중단!
	if steps > n:
		# 그리고, 지금까지의 발자국 조합을 출력한다.
		for item in footprint:
			print(item, end=' ')
		print()
		return
	for i in range(len(dist)):	# 보폭의 종류는 3가지 (30, 50, 70cm). 즉, 사실상 constant value인 3이나 마찬가지다. 하지만, 추후 확장성을 위해서 len() 함수를 이용.
		if prev != i:	# (1)번 조건을 위한 조건식 -> 방금전에 선택한 보폭은 이번에 선택하지 않는다!	prev 값을 넘겨주어서, 다음 단계의 보폭과 겹치지 않게 함.
			if not check(footprint, i):
				footprint.append(dist[i])
				pengsu(steps+1, i, footprint)
				footprint.pop()

# 발 걸음 수 n을 입력받는다.
n = int(input())

# 움직일 수 있는 보폭(한 걸음 당 거리) 정의:
dist = [30, 50, 70]

# 발자국 정보를 저장할 리스트 정의:
footprint = []

# 재귀 함수 호출!
pengsu(1, -1, footprint)
