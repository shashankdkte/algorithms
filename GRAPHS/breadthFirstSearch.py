#TIME COMPLEXITY 0(V+E)
#SPACE COMPLEXITY O(V)

class Node:
    def __init__(self,name):
        self.children = []
        self.name = name

    def addChild(self,name):
        self.children.append(Node(name))    

    def breadthFirstSearch(self,array):
        # CREATE QUEUE
        queue =[self]
        # LOOP TILL QUEUE IS NOT EMPTY
        while len(queue) > 0:
            #GET FIRST NODE
            current = queue.pop(0)
            # ADD TO ARRAY
            array.append(current.name)
            # ADD ITS CHILDREN TO QUEUE
            for child in current.children:
                queue.append(child)
        return array             
