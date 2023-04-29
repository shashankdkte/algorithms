#TIME COMPLEXITY O(N^2)
#SPACE COMPLEXITY O(1)
def twoNumberSum(array,targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(len(array)):
            secondNum = array[j]
            if(firstNum + secondNum == targetSum):
                return [firstNum,secondNum]
    return []       

#TIME COMPLEXITY O(N)
#SPACE COMPLEXITY O(N)
def twoNumberSum(array,targetSum):
    nums ={}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch,num]
        else:
            nums[num] = True
    return []                

#TIME COMPLEXITY O(NLOGN)
#SPACE COMPLEXITY O(1)
def twoNumberSum(array,targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
          return [array[left],array[right]]
        elif currentSum < targetSum:
            left = left + 1
        elif currentSum > targetSum:
            right-=1
    return []         
