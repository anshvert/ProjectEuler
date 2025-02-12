def pal(num):
    return str(num) == str(num)[::-1]

maxP = float("-inf")

# Six digit palindrome takes form of 11 * (9091a + 910b + 100c)
for i in range(990,99,-11):
    for j in range(999,99,-1):
        prod = i*j
        if prod < maxP:
            break
        if pal(prod):
            maxP = max(maxP,prod)
            break

print(maxP)

