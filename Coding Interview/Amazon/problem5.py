# 5. Level Order Traversal of Binary Tree

# Given the root of a binary tree, display the node values at each level.
# Node values for all levels should be displayed on separate lines.
# Let’s take a look at the below binary tree.

# Level order traversal for this tree should look like: 100; 50, 200; 25, 75, 350
from queue import Queue


class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = TreeNode(data)

    def lfs(self):
        elements = []

        if self.left:
            elements += self.left.lfs()

        if self.right:
            elements += self.right.lfs()

        elements.append(self.data)

        return elements

    def bfs(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.bfs()

        if self.right:
            elements += self.right.bfs()

        return elements

    def dfs(self):
        elements = []

        if self.left:
            elements += self.left.dfs()

        elements.append(self.data)

        if self.right:
            elements += self.right.dfs()

        return elements


def build_tree(elements):
    root = TreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


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


if __name__ == '__main__':
    arr = [100, 50, 200, 25, 75, 350]
    tree = build_tree(arr)
    print(tree.lfs())
    print(tree.bfs())
    print(tree.dfs())
    print(level_order_traversal(tree))
