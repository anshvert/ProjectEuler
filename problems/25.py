x1,x2 = 1,1
fbc = 2

while len(str(x2)) < 1000:
    x1,x2 = x2,x1+x2
    fbc += 1
print(fbc)