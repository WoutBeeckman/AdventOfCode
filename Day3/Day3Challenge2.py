# Checks 3 given strings and checks for the same letter
def findSameLetter(line1, line2, line3):
    for letter in line1:
        if (letter) in (line2) and (letter) in (line3):
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

# Takes 3 lines, finds same letter, translates the letter to it's prority, adds the priority to the score, and move to the next tree letters