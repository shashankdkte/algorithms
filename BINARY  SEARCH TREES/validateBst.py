#TIME COMPLEXITY
#O(n)
#SPACE COMPLEXITY
#O(d)
def validatebst(tree):
    return  validateBstHelper(tree,float("-inf"),float("inf"))

def validateBstHelper(tree,minvalue,maxValue):
  # LEAF NOFE
  if tree is None:
     return True;
# 10 <= node.value < 15 where node.value is 13
  if tree.value < minvalue or tree.value>=maxValue:
     return False
  leftIsValid = validateBstHelper(tree.left,minvalue,tree.value)
  rightIsValid = validateBstHelper(tree.right,tree.value,maxValue)
  return leftIsValid and rightIsValid 