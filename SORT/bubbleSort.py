# TIME COMPLEXITY O(n^2)
# SPACE COMPLEXITY O(1)
def bubbleSort(array):
    isSorted=False
    for i in range(len(array)-1):
        if isSorted == True:
            break
        isSorted = True
        for j in range(len(array) - 1 - i):
            if array[i] >array[i+1]:
                swap(i,i+1,array)
                isSorted = False
    return array


def swap(i,j,array):
    array[i],array[j] = array[j],array[i]