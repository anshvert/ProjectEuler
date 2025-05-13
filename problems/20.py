factorial = 1
for i in range(1, 101):
    factorial *= i

digit_sum = sum(int(d) for d in str(factorial))
print(digit_sum)