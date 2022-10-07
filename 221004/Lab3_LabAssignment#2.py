#어렵지는 않았지만 파일입출력때매올림
#펭수 바리케이트 어쩌구 하는 문제
#텍스트파일에는 위치 수 n이랑 각 위치에 있는 블럭 수가 있음
fin = open('barricade.txt', 'r')

block = []
line = fin.readline()
line = line.split('\n')
n = int(line[0])
line = fin.readline()
in_blocks = line.split(' ')
for item in in_blocks:
    block.append(int(item))
fin.close()

k = 0
floor = int(sum(block) / n)
for i in range(0, n):
    if block[i] > floor:
        k += block[i] - floor
print('The minimum number of moves is ', k, '.', sep='')
