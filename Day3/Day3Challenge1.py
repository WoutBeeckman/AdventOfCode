import re

# Split the Rucksack in halve (two compartments so two strings)
def splitString(string):
    middle = int(len(string) / 2)
    firstString = string[:middle]
    secondString = string[middle:]
    return firstString, secondString

# Find which item appears in both strings (aka compartments)

# Translate the item to it`s priority

# Loop through all lines, split each line, find double items, translate to priority, calculate total score
