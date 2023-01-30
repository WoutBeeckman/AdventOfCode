import re

# Get all point from the chosen shape
def getScoreFromShape(inputFile):
    score = 0
    with open(inputFile) as file:
        for line in file:
            if re.match(r".*X", line):
                score += 1
            elif re.match(r".*Y", line):
                score += 2
            else:
                score += 3
    return score

# print(getScoreFromShape("testData"))

# Get all point from winning the matches, form the perspective of the second hand aka your hand
def getScoreFromWinning(inputFile):
    score = 0
    with open(inputFile) as file:
        for line in file:
            opponentShape = line[0]
            myShape = line[2]
            # Check if it's a draw
            if (opponentShape, myShape) in [("A", "X"), ("B", "Y"), ("C", "Z")]:
                score += 3
            # Check if you win
            elif (opponentShape, myShape) in [("C","X"), ("A", "Y"), ("B","Z")]:
                score += 6
    return score

# print(getScoreFromWinning("testData"))

print(getScoreFromShape("Day2Input.txt") + getScoreFromWinning("Day2Input.txt"))
