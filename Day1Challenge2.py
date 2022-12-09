import re
# Day 1: Calorie Counting

# Count all lines not seperated by a new line together
caloriesPerReindeer = []

def totalCalories(inputFile):
    with open(inputFile) as file:
        reindeer = 0
        for line in file:
            if line != "\n":
                reindeer += int(line)
            else:
                caloriesPerReindeer.append(reindeer)
                reindeer = 0
# Find the 3 biggest numbers
def findTop3(caloriesPerReindeer):
    # Declare the top 3
    top1 = 0
    top2 = 0
    top3 = 0
    # Loop through caloriesPerReindeer and compare them to all the top 3 (starting with the first)
    for reindeer in caloriesPerReindeer:
        if reindeer > top1:
            top1 = reindeer
        elif reindeer > top2:
            top2 = reindeer
        elif reindeer > top3:
            top3 = reindeer

