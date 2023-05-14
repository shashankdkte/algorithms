# TIME COMPLEXITY O(n^2)
#SPACE COMPLEXITY O(n)
def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString

# TIME COMPLEXITY O(n)
#SPACE COMPLEXITY O(n)
def isPalindrome(string):
    reversedChars  = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)

# TIME COMPLEXITY O(n)
#SPACE COMPLEXITY O(n)
def isPalindrome(string,i=0):
    j = len(string)- 1 - i
    return True if i>=j else string[i] == string[j] and isPalindrome(string,i+1)

# TIME COMPLEXITY O(n)
#SPACE COMPLEXITY O(1)
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
      if string[leftIdx] != string[rightIdx]:
          return False
      leftIdx +=1
      rightIdx -=1
    return True