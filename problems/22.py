with open("./22.txt", "r") as f:
    for line in f.readlines():
        nameList = sorted(line.strip("\n").split(','))
        totalScore = 0
        for ind,name in enumerate(nameList):
            nameScore = 0
            for ch in name[1:-1]:
                nameScore += ord(ch) - ord('A') + 1
            totalScore += (nameScore * (ind+1))
        print(totalScore)
