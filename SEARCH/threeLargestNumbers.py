def findThreeLargestNumbers(array):
    threeLargestNumbers = [None,None,None]
    for num in array:
        updateLargest(threeLargestNumbers,num)
    return threeLargestNumbers    

def updateLargest(threeLargest,num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest,num,2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest,num,2)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest,num,2)        

def shiftAndUpdate(array,num,idx):
    for i in range(idx+1):
        if i  == idx:
            array[idx]=num
        else:
            array[i] = array[i+1]