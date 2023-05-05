class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

#TIME COMPLEXITY O(N)
# SPACE COMPLEXITY O(1)
def removeDuplicatesFromLinkedList(linkedList):
    #GET CURRENT NODE
    currentNode = linkedList
    # GO THROUGH LIST TILL CURRENT NODE IS NOT NONE
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        # LOOP TILL YOU FIND NEXT DISTINCT VALUE
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next

        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
    
    return linkedList
