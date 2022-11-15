#하노이의탑 정리하기... 개어렵ㄴㅔ
def hanoi(n, to_): # 하노이 원본이랑 다르게 옮겨줄 곳만 입력받음. 첨엔 셋 다 입력하는 걸로 시작했는데 생각해보니까 좀 비효율적인듯
    if n == 0:
        return
    
    from_ = findPlace(n) # n번째 원반이 현재 어디 있는지 찾고

    if from_ == to_: # 그게 이미 목적지에 있다면
        hanoi(n-1, to_) # n번쨰 원반에 대해서는 아무것도 안하고 그냥 다음 원반으로 넘어감
        return

    aux_ = 6 - from_ - to_ # 지금 n번째 원반이 목적지 말고 다른 곳에 있으면 목적지로 옮겨줘야함. 그러기 위해서 임시기둥이 어딘지 설정해줌
    # 여기서부터는 일반 하노이탑 원리랑 똑같음
    hanoi(n-1, aux_) # n-1개의 원반을 임시기둥으로 옮겨주고
    print(n,': ', from_, ' >> ', to_, sep='') # n번째 원반을 목표기둥에 옮겨준 다음
    move(n, from_, to_) # 실제로 n번쩆 원반을 옮겨줘서 리스트를 업데이트 해줘야함. 재귀 한번마다 하나씩 옮기는게 맞음. 첨엔 세번 옮겻는데 이러면 논리상 안맞은ㅁ
    global cnt
    cnt += 1
    hanoi(n-1, to_) # 임시기둥에 옮겨뒀던 n-1개의 원반을 목표기둥에 옮겨줌.

def findPlace(n):
    for i in range(3):
        if n in column[i]:
            return i+1

def move(movenum, _from, _to):
    column[_from-1].pop()
    column[_to-1].append(movenum)

column = []
max = 0
cnt = 0
for i in range(3):
    line = [int(item) for item in input().split()]
    column.append(line)
    max += len(line)
    
#for i in range(3):
#    column.append(list(map(int, input().split())))
# 이런식으로 입력받는ㄱㅔ 더 간단할듯ㅅ. map이랑 list자료변환하는거 사용하기    

hanoi(max, 3)
print(cnt)
