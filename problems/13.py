currentNum = ""

def add(num):
    global currentNum
    if not len(currentNum):
        currentNum = num
        return
    ns,cry = "",0
    num = ('0' * (len(currentNum) - len(num))) + num
    for i in range(len(num)-1,-1,-1):
        sm = int(num[i]) + int(currentNum[i]) + cry
        ns += str(sm % 10)
        cry = sm // 10
    if cry: ns += str(cry)
    currentNum = ns[::-1]

with open("./13.txt", "r") as file:
    for num in file:
        #print(num)
        add(num.strip('\n'))
    print(currentNum[:10])