from queue import Queue


class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def dfs(self):
        elements = []

        if self.left:
            elements += self.left.dfs()

        elements.append(self.data)

        if self.right:
            elements += self.right.dfs()

        return elements


def level_order_traversal(root):
    elements = []
    if root == None:
        return

    Q = Queue()
    Q.put(root)

    while not Q.empty():
        node = Q.get()
        if node == None:
            continue
        elements.append(node.data)
        Q.put(node.left)
        Q.put(node.right)

    return elements


def is_bst(root):
    element = root.right

    while element:
        if element.data < root.data:
            return False
        element = element.left

    return True


if __name__ == '__main__':
    root1 = TreeNode(100)
    root1.left = TreeNode(50)
    root1.right = TreeNode(200)
    root1.left.left = TreeNode(25)
    root1.left.right = TreeNode(75)
    root1.right.left = TreeNode(125)
    root1.right.right = TreeNode(350)

    root2 = TreeNode(100)
    root2.left = TreeNode(50)
    root2.right = TreeNode(200)
    root2.left.left = TreeNode(25)
    root2.left.right = TreeNode(75)
    root2.right.left = TreeNode(90)
    root2.right.right = TreeNode(350)

    # print(root.dfs())
    # print(level_order_traversal(root))
    print(is_bst(root1))
    print(is_bst(root2))
