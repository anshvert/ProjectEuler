mat = [[0]*21 for _ in range(21)]
mat[0][0] = 1

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i == 0 and j == 0: continue
        upr = mat[i-1][j] if i-1 >= 0 else 0
        left = mat[i][j-1] if j-1 >= 0 else 0
        mat[i][j] = upr + left

#print(mat)
print(mat[-1][-1])