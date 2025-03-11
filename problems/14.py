limit,ans,ansNum = 1000000,0,None

def getChainLength(number):
    count = 0
    while number != 1:
        if number % 2:
            number = number*3 + 1
        else:
            number //= 2
        count += 1
    return count + 1

for num in range(2,limit):
    chain_length = getChainLength(num)
    if chain_length > ans:
        ans = chain_length
        ansNum = num

print(ansNum)