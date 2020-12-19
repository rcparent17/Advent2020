numTrees = 0
treeMap = []

with open("3.input", "r") as trees:
    treeMap.extend([x.strip() for x in trees])

mapWidth = len(treeMap[0])
tobogR = 1
tobogC = 3

while tobogR < len(treeMap):
    if treeMap[tobogR][tobogC] == "#":
        numTrees += 1
    tobogR += 1
    tobogC = (tobogC + 3) % mapWidth

print("Number of trees encountered: " + str(numTrees))
