#TIME COMPLEXITY O(nlogn)
#SPACE COMPLEXITY O(n)
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx];
        sortedSquares[idx] = value * value
    sortedSquares.sort()
    return sortedSquares    

#TIME COMPLEXITY O(n)
#SPACE COMPLEXITY O(n)
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    leftIndex = 0
    rightIndex = len(array) - 1

    for idx in reversed(range(len(array))):
        if abs(leftIndex) > abs(rightIndex):
            value = array[leftIndex];
            sortedSquares[idx] = value * value
            leftIndex+=1
        else:
            value = array[leftIndex];
            sortedSquares[idx] = value * value
            rightIndex-=1    
    return sortedSquares    