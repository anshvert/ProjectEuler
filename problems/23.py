def sumDivisors(num):
    sm = 0
    for div in range(2,int(num**0.5)+1):
        if num % div == 0:
            if div == num // div:
                sm += div
            else:
                sm += div
                sm += num // div
    return sm + 1

limit = 28123

abundantNums = []
for i in range(1,limit+1):
    if sumDivisors(i) > i:
        abundantNums.append(i)

ttlSum = (limit * (limit + 1)) // 2
st = set()

for i in range(len(abundantNums)):
    for j in range(i,len(abundantNums)):
        num = abundantNums[i] + abundantNums[j]
        if num in st:
            continue
        st.add(num)
        if num <= limit:
            ttlSum -= num

print(ttlSum)