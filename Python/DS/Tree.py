class Node:
    def __init__(self, val):
        self.childLeft = None
        self.childRight = None
        self.nodeData = val
    
root = Node(1)
root.childLeft = Node(2)
root.childRight = Node(3)
root.childLeft.childLeft = Node(4)
root.childLeft.childRight = Node(5)
root.childRight.childLeft = Node(6)
root.childRight.childRight = Node(7)

# In Order Traversal
def InOrder(root):
    if root:
        InOrder(root.childLeft)
        print(root.nodeData)
        InOrder(root.childRight)

print("In-Order Traversal")
InOrder(root)
print("\n")


# Pre Order Traversal
def PreOrder(root):
    if(root):
        print(root.nodeData)
        PreOrder(root.childLeft)
        PreOrder(root.childRight)

print("Pre-Order Traversal")
PreOrder(root)
print("\n")


# Post Order Traversal
def PostOrder(root):
    if root:
        PostOrder(root.childLeft)
        PostOrder(root.childRight)
        print(root.nodeData)

print("Post-Order Traversal")
PostOrder(root)
print("\n")