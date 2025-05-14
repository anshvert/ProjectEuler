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

st,ans = set(),0

for i in range(1,10**4):
    sumDiv = sumDivisors(i)
    if (sumDiv,i) in st:
        ans += (i + sumDiv)
        print(i,sumDiv)
    st.add((i,sumDiv))

print(ans)