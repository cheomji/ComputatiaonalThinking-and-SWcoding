#오목 결과 판정하는 프로그램
#test file (baduk.txt)
###############
######X########
#OXXXXO########
####OXO########
###OXOOX#######
####XXOO#######
#####OOO#######
####O###X######
###O###########
##X############
###############
###############
###############
###############
###############
#초반에 너무 복잡하게 생각해서 꼬임ㅉㅉ 파일입출력 어케하는지도 봐 놓자
fin = open('baduk.txt', 'r')
baduk = []
while True:
    line = fin.readline()
    if not line: break
    line = line.split('\n')
    baduk_line = []
    for item in line[0]:
        baduk_line.append(item)
    baduk.append(baduk_line)

for i in range(0, 15):
    w_hor = 0
    w_ver = 0
    b_hor = 0
    b_ver = 0
    for j in range(0, 14):
        if baduk[i][j] == baduk[i][j+1] == 'O':
            w_hor += 1
        if baduk[j][i] == baduk[j+1][i] == 'O':
            w_ver += 1
        if baduk[i][j] == baduk[i][j+1] == 'X':
            b_hor += 1
        if baduk[j][i] == baduk[j+1][i] == 'X':
            b_ver += 1
    #print(w_hor, b_hor, w_ver, b_ver)
    if w_hor == 4 or w_ver == 4:
        print('* White player win!')
        break
    elif b_hor == 4 or b_ver == 4:
        print('* Black player win!')
        break
    
fin.close()
