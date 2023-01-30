import re

# Get all point from the chosen shape
def getScoreFromShape(inputFile):
    score = 0
    with open(inputFile) as file:
        for line in file:
            if line == ".*X":
                score += 1
            elif line == ".*Y":
                score += 2
            else:
                score += 3

getScoreFromShape("testData.txt")