import re
# Check what shape you need and return them in a list
def getChosenShapes(inputFile):
    shapes = []
    with open(inputFile) as file:
        for line in file:
            if re.match(r".*X", line):
                if re.match(r"A.*", line):
                    shapes.append("Z")
                elif re.match(r"B.*", line):
                    shapes.append("X")
                else:
                    shapes.append("Y")
            elif re.match(r".*Y", line):
                if re.match(r"A.*", line):
                    shapes.append("X")
                elif re.match(r"B.*", line):
                    shapes.append("Y")
                else:
                    shapes.append("Z")
            elif re.match(r".*Z", line):
                if re.match(r"A.*", line):
                    shapes.append("Y")
                elif re.match(r"B.*", line):
                    shapes.append("Z")
                else:
                    shapes.append("X")
    return shapes
# print(getChosenShapes("testData"))

# Check the list with chosen shapes, and calculate points
def getPointsFromShapes(shapes):
    score = 0
    for shape in shapes:
        if shape == "X":
            score += 1
        elif shape == "Y":
            score += 2
        else:
            score += 3
    return score
# print(getPointsFromShapes(getChosenShapes("testData")))

# Calculate all wins and draws
def getPointsFromWinning(inputFile):
    score = 0
    with open(inputFile) as file:
        for line in file:
            myShape = line[2]
            # Check if it's a draw
            if myShape == "Y":
                score += 3
            # Check if you win
            elif myShape == "Z":
                score += 6
    return score
# print(getPointsFromWinning("testData"))
