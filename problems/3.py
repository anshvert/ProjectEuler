number = 600851475143

def getPrimeFactor(num):
    maxP = 1
    while num:
        if num % 2 == 0:
            num //= 2
            maxP = 2
        else:
            for i in range(3,int(num**0.5),2):
                #print(i)
                while num % i == 0:
                    #print(num)
                    num //= i
                    maxP = max(maxP,i)
            break
    return maxP

print(getPrimeFactor(number))