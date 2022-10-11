def binaryToDecimal(numBinary):
    numDecimal = 0
    for i in range(0, len(numBinary)):
        numDecimal += numBinary[i] * (2 ** (len(numBinary)-1-i))
    return numDecimal

nums = [1,0,0,1]
print(f'bunaryToDecinal({nums}):', binaryToDecimal(nums))

nums = [1,1,1,1,1]
print(f'bunaryToDecinal({nums}):', binaryToDecimal(nums))

nums = [1,0,1,0,1]
print(f'bunaryToDecinal({nums}):', binaryToDecimal(nums))
