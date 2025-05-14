# Calculates Next Permutation for String
def nextPermutation(numS):
    piv = None
    for i in range(len(numS)-1):
        if int(numS[i]) < int(numS[i+1]):
            piv = i
    if piv is None:
        print(numS)
        return ""
    pivSwap = piv+1
    for i in range(pivSwap,len(numS)):
        if int(numS[pivSwap]) > int(numS[i]) > int(numS[piv]):
            pivSwap = i
    numS[pivSwap],numS[piv] = numS[piv],numS[pivSwap]
    numS[piv+1:] = sorted(numS[piv+1:])
    return "".join(numS)

iniString = '0123456789'
for i in range(999999):
    iniString = nextPermutation(list(iniString))
    if not iniString:
        break
print(iniString)
