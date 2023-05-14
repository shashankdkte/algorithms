# TIME COMPLEXITY O(n)
#SPACE COMPLEXITY O(n)
def runningEncoding(string):
    encodedStringCharacters = []
    currentLength = 1

    for i in range(1,len(string)):
        currentCharacter = string[i]
        previousCharracter = string[i-1]

        if currentCharacter != previousCharracter or currentLength == 9:
            encodedStringCharacters.append(str(currentLength))
            encodedStringCharacters.append(str(previousCharracter))
            currentLength = 0

        currentLength +=1

    encodedStringCharacters.append(str(currentLength))
    encodedStringCharacters.append(string[len(string) - 1])       

    return "".join(encodedStringCharacters) 