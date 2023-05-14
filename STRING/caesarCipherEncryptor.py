# TIME COMPLEXITY O(n)
#SPACE COMPLEXITY O(n)
def caesarCipherEncryptor(string,key):
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetters(letter,newKey))
    return "".join(newLetters)    
def getNewLetters(letter,key):
    newLetter = ord(letter) + key
    return chr(newLetter) if newLetter <= 122 else chr(96 + newLetter % 122)


def caesarCipherEncryptor(string,key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetters(letter,newKey,alphabet))
    return "".join(newLetters)    
def getNewLetters(letter,key,alphabet):
    newLetter = alphabet.index(letter) + key
    return alphabet[newLetter] if newLetter <= 122 else alphabet[-1 + newLetter % 25]