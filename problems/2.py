limit = 4000000 # 4 mil

def fib(l):
    arr = [1,1]
    while arr[-1] < l:
        arr.append(arr[-1] + arr[-2])
    return arr

def main():
    arr = fib(limit)
    count = 0
    print(arr)
    for i in arr:
        if i % 2 == 0:
            count += i
    print(count)

main()