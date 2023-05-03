#ITERATIVE APPROACH
#TIME COMPLEXTITY O(n)
#SPACE COMPLEXITY O(h)
def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node":root,"depth":0}]
    while len(stack) >0:
        nodeInfo = stack.pop();
        node = nodeInfo["node"]
        depth = nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths = sumOfDepths + depth
        stack.append({"node":node.left,"depth": depth+ 1})
        stack.append({"node":node.right,"depth": depth+ 1})

def nodeDepths(root,depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left , depth + 1) + nodeDepths(root.right , depth + 1)