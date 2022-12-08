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
# Loop through all lines and remember the biggest number
def getBiggest(list):
    biggestReindeer = 0
    for reindeer in list:
        if reindeer > biggestReindeer:
            biggestReindeer = reindeer
    print(biggestReindeer)

totalCalories("Day1Input.txt")
getBiggest(caloriesPerReindeer)
#print(caloriesPerReindeer)
