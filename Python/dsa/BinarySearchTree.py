class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    # DFS
    def inOrder_Traversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrder_Traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inOrder_Traversal()

        return elements


    def search(self, value):
        if self.data == value:
            return True
        # print(self.data)
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def min_value(self):
        if self.left is None:
            return self.data
        return self.left.min_value()

    def max_value(self):
        if self.right is None:
            return self.data
        return self.right.max_value()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else: 
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.left
            if self.right is None:
                return self.right

            min_val = self.right.min_value()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 2, 19, 5, 6, 4, 15]

    numbers_tree = build_tree(numbers)
    print(numbers_tree.inOrder_Traversal())

    print(numbers_tree.search(5))
    print(numbers_tree.search(21))

    print("Max", numbers_tree.max_value())
    print("Min", numbers_tree.min_value())

    numbers_tree.delete(6)
    print(numbers_tree.inOrder_Traversal())
