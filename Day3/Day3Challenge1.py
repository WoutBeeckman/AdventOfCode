import re

# Split the Rucksack in halve (two compartments so two strings)
def splitString(string):
    middle = int(len(string) / 2)
    firstString = string[:middle]
    secondString = string[middle:]
    return firstString, secondString

# Find which item appears in both strings (aka compartments)
def findSameLetter(firstString, secondString):
    for letter in firstString:
        if (letter) in (secondString):
            return letter

# Translate the item to it`s priority
def translateToPriority(letter):
    priorityUpercase = [27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
    lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if letter.islower():
        return lowercase.index(letter) + 1
    else:
        index = uppercase.index(letter)
        return priorityUpercase[index]

# Loop through all lines, split each line, find double items, translate to priority, calculate total score
