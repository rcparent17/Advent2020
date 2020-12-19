treeMap = []

slopes = []
slopes.append([1, 1])
slopes.append([1, 3])
slopes.append([1, 5])
slopes.append([1, 7])
slopes.append([2, 1])

slopeTrees = [0] * len(slopes)

with open("3.input", "r") as trees:
    treeMap.extend([x.strip() for x in trees])

mapWidth = len(treeMap[0])

for i in range(len(slopes)):
    tobogR = slopes[i][0]
    tobogC = slopes[i][1]

    while tobogR < len(treeMap):
        if treeMap[tobogR][tobogC] == "#":
            slopeTrees[i] += 1
        tobogR += slopes[i][0]
        tobogC = (tobogC + slopes[i][1]) % mapWidth

mult = slopeTrees[0]
for i in range(1, len(slopeTrees)):
    mult *= slopeTrees[i]

print("Number of trees encountered: {}\n\nResult: {}".format(str(slopeTrees), mult))
