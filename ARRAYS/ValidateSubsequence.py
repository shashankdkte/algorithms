#TIME COMPLEXITY O(N)
#SPACE COMPLEXITY O(1)
def validateSubSequnce(array,sequence): 
    arrIdx = 0
    seqIdx = 0
    while arrIdx<len(array) and seqIdx < len(array):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx+=1
        arrIdx+=1
    return seqIdx == len(sequence)  

#TIME COMPLEXITY O(N)
#SPACE COMPLEXITY O(1)
def validateSubSequnce(array,sequence): 
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx+=1

    return seqIdx == len(sequence)  