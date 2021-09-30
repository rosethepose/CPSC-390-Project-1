class Node:
    def __init__(self, state, parent = None, pathCost = None, children = None):
        self.state = state
        self.parent = parent #node list of parents
        self.pathCost = pathCost #assumed that the amt of costs matches amt of children
        self.depth = 0 #depth is zero if it is the root node
        self.children = children

        if parent: #if the parent list is not null it means it is not the root node
            temp : Int = 1000 #we want to have a temp value for the depth to comapre
            for p in parent: #take the shortest depth out of any of the nodes
                if p and (temp > p.depth):
                    temp = p.depth
            self.depth = temp + 1 #initialize depth to the shortest depth +1 for itself


#declare the tree
nodeS = Node(state='S')
nodeA = Node(state='A', pathCost=[3], parent=[nodeS, None, None])
nodeB = Node(state='B', pathCost=[1], parent=[nodeS, None, None])
nodeC = Node(state='C', pathCost=[8], parent=[nodeS, None, None])

nodeS.children=[nodeA,nodeB,nodeC] #add children seperately

nodeD = Node(state='D', pathCost=[3], parent=[nodeA, None, None])
nodeE = Node(state='E', pathCost=[7], parent=[nodeA, None, None])
nodeG = Node(state='G', pathCost=[15, 20, 5], parent=[nodeA,nodeB,nodeC])

nodeA.children=[nodeD,nodeE,nodeG]
nodeB.children=[nodeG, None, None]
nodeC.children=[nodeG, None, None]


def breadthFirstSearch( tree, queue = [] ):
    if(tree.state == 'G'):
        print("Found!")
        return
    if(tree.state != 'G'):
        if (tree.children): # if my tree has children, expand the nodes and add to queue
            for x in tree.children:
                if(x and x not in queue):
                    queue.append(x)
        if queue: #if my queue is not empty, pop the first node and continue search
            node = queue.pop(0) #we always pop the first value off the queue
            breadthFirstSearch(node, queue)

breadthFirstSearch(nodeS)
