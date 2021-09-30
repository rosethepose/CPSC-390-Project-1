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


#    def addChild(self, newNode):
#        newNode.parent.append(self)
#        newNode.depth = self.depth + 1
#        self.children.append(newNode)

    def show(self):
        for i in self.children:
            print(i.state)


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

#print(nodeD.depth)

#nodeS.show()
#nodeA.show()


#Depth-first Search
#Expand the deepest unexpanded node, “leftmost” solution
#Implemented with a LIFO queue
#Time complexity: O(bm)

def depthFirstSearch( tree, cost = 0 ):
    stack = []
    print("State: ",tree.state) #for testing
    if tree.state == 'G': #if we found the goal, return cost
        return cost;
    else:
        if (tree.children): #make sure we arent at a leaf node
            for i in range (2,0) : #loop through the list of children
                if(tree.children[i]): #if child is not null, otherwise go to next
                    stack.append(tree.children[i]) #append all current children to the stack

            cost += tree.children[0].pathCost[0]
            depthFirstSearch(tree.children[0], cost)
            stack.remove(tree.children[0])

def breadthFirstSearch( tree, queue = [] ):
    #queue = []
    #print("State; ",tree.state)
    #print(tree.state, " state is",tree.state == 'G')
    if(tree.state == 'G'):
        print("Found!")
        return
    if(tree.state != 'G'):
        if (tree.children): # if my tree has children, expand the nodes and add to queue
            for x in tree.children:
                if(x and x not in queue):
                    queue.append(x)
        if queue:
        #for _ in queue: #iterate through queue
            node = queue.pop(0) #we always pop the first value off the queue
            print(node.state, " popped")
            breadthFirstSearch(node, queue)

breadthFirstSearch(nodeS)
