import random
import string

TARGET = raw_input("Enter a string for monkeys to type: ").upper()
TARGET_LEN = len(TARGET)
LETTERS = string.ascii_uppercase + " " + string.punctuation
GENERATIONS = 100

matchingList = []

randomStrings = []

bestString = {
    'string': '',
    'base_for_new_generation': '',
    'score': 0
}

def randomString(stringLength):
    return ''.join(random.choice(LETTERS) for i in range(stringLength));

def replaceNoneMatchesWithRandom():
    tempString = bestString['base_for_new_generation']
    for i, letter in enumerate(tempString):
        if letter == '*':
            tempString = switchChar(tempString, i, random.choice(LETTERS))
    return tempString

def switchChar(string, index, rand_char):
    return string[:index]+rand_char+string[index+1:]

def createNewGeneration():
    generation = []
    replaceNoneMatches()
    for i in range(100):
        generation.append(replaceNoneMatchesWithRandom())
    randomStrings.append(generation)

def createMatchingList(stringLength):
    for i in range(stringLength):
        matchingList.append(False)

def replaceNoneMatches():
    base_for_new_generation = ''
    for i in range(TARGET_LEN):
        if TARGET[i] == bestString['string'][i]:
            base_for_new_generation = base_for_new_generation + bestString['string'][i]
        else:
            base_for_new_generation = base_for_new_generation + '*'
    bestString['base_for_new_generation'] = base_for_new_generation

def checkMatch():
    latest_generation = randomStrings[-1]
    for string in latest_generation:
        score = 0
        for letter in TARGET:
            for i in range(TARGET_LEN):
                if TARGET[i] == string[i]:
                    score = score + 1

        if score > bestString['score']:
            bestString['string'] = string
            bestString['score'] = score

def createInitialStrings():
    generation = []
    for i in range(100):
        string = randomString(TARGET_LEN)
        generation.append(string)
    randomStrings.append(generation)

def printBestString():
    print('Generation ' + str(len(randomStrings)))
    print('Current best string ' + bestString['string'])

def start():
    createInitialStrings()
    checkMatch()
    printBestString()
    for i in range(GENERATIONS):
        if bestString['string'] == TARGET:
            print("Script Complete Matched in " + str(1+len(randomStrings)) + " generations")
            printBestString()
            break
        createNewGeneration()
        checkMatch()
        printBestString()

start()
