def binaryToDecimal(numBinary):
    numDecimal = 0
    for i in range(0, len(numBinary)):
        numDecimal += numBinary[i] * (2 ** (len(numBinary)-1-i))
    #교수님 코드
    #lst = [i**2 for i in range(len(numBinary)-1, -1, -1)] -> 16 8 4 2 1 이런 리스트 만들어주는거
    #for d in lst: 이렇게 해서 ... 어 .. numBinary 요소들 돌면서 저거 곱해주면됨ㅇㅇ
    return numDecimal

nums = [1,0,0,1]
print(f'bunaryToDecinal({nums}):', binaryToDecimal(nums))

nums = [1,1,1,1,1]
print(f'bunaryToDecinal({nums}):', binaryToDecimal(nums))

nums = [1,0,1,0,1]
print(f'bunaryToDecinal({nums}):', binaryToDecimal(nums))
