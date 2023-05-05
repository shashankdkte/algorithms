# TIME COMPLEXITY O(n)
# SPACE COMPLEXITY O(1)
def middleNode(linkedlist):
    count = 0
    currentNode = linkedlist
    middleNode = linkedlist;
    while currentNode is not None:
        count +=1
        currentNode = currentNode.next
    
    for _ in range(count//2):
        middleNode = middleNode.next

    return middleNode
# TIME COMPLEXITY O(n)
# SPACE COMPLEXITY O(1)
def middleNode(linkedlist):
    slowNode = linkedlist
    fastNode = linkedlist
    while fastNode is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    return slowNode    