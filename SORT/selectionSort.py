# TIME COMPLEXITY O(n^2)
# SPACE COMPLEXITY O(1)
def selectionSort(array):
    for i in range(len(array)):
        smallestIdx = i
        for j in range(i + 1,len(array)):
            if array[smallestIdx] > array[j]:
                smallestIdx = j
        swap(i,smallestIdx,array)
    return array
        

def swap(i,j,array):
    array[i],array[j] = array[j],array[i]