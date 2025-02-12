grid = []
with open("11.txt","r") as file:
    for line in file:
        grid.append(line.strip("\n").split(" "))

maxP = 0
def getProd(i,j,dx,dy):
    prod = 1
    for ii in range(4):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            prod *= int(grid[i][j])
            i += dx
            j += dy
        else:
            prod = 0
            break
    return prod

for i in range(len(grid)):
    for j in range(len(grid[0])):
        rightProd = getProd(i,j,0,1)
        rightDig = getProd(i,j,1,1)
        bottomProd = getProd(i,j,1,0)
        bottomDig = getProd(i,j,1,-1)
        prod = max(rightProd, rightDig, bottomProd, bottomDig)
        maxP = max(maxP, prod)

print(maxP)

