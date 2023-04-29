#TIME COMPLEXITY O(logn)
#SPACE COMPLEXITY O(1ogn)

#WORST
#TIME COMPLEXITY O(n)
#SPACE COMPLEXITY O(n)
def findClosestValueInBst(tree,target):
    return findClosestValueInBstHelper(tree,target,float("inf"))

def findClosestValueInBstHelper(tree,target,closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest =tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left,target,closest)  
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right,target,closest)
    else:
        return closest
    

#TIME COMPLEXITY O(logn)
#SPACE COMPLEXITY O(1)

#WORST
#TIME COMPLEXITY O(n)
#SPACE COMPLEXITY O(1)

def findClosestValueInBst(tree,target):
    return findClosestValueInBstHelper(tree,target,float("inf"))

def findClosestValueInBstHelper(tree,target,closest):
    currentNode = tree
    while currentNode is not None:
      if abs(target - closest) > abs(target -  currentNode.value):
          closest = currentNode.value
      if target <  currentNode.value:
          currentNode = currentNode.left
      elif target >  currentNode.value:
          currentNode = currentNode.right
      else:
          break
    return closest
    