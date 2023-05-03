class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#TIME COMPLEXITY
#O(n)
#SPACE COMPLEXITY
#O(d) d->depth of the tree
# distance of deepest node 
def branchSums(root):
    sums  = []
    calculateBranchSums(root,0,sums)
    return sums

def calculateBranchSums(node,runningSum,sums):
    if node is None:
        return 
    
    runningSum = runningSum + node.value
    # NODE IS LEAF 
    if node.left is None and node.right is None:
        sums.append(runningSum)

    #IF NODE IS NOT LEAF
    calculateBranchSums(node.left,runningSum,sums)
    calculateBranchSums(node.right,runningSum,sums)