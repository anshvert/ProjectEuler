from meth import divisors_count

currentNum,seq = 0,0

while divisors_count(currentNum) <= 500:
    currentNum += seq
    seq += 1

print(currentNum)
