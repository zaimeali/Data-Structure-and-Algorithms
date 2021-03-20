class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1

        return level

    def print_indentation(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_indentation()


def build_product_tree():
    root = TreeNode("Apple")

    laptop = TreeNode("Computer")
    laptop.add_child(TreeNode("Mac Book"))
    laptop.add_child(TreeNode("iMac"))

    mobile = TreeNode("Mobile")
    mobile.add_child(TreeNode("iPhone 7"))
    mobile.add_child(TreeNode("iPhone 8"))
    mobile.add_child(TreeNode("iPhone X"))
    mobile.add_child(TreeNode("iPhone XI"))

    watch = TreeNode('Watch')
    watch.add_child(TreeNode("iWatch"))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(watch)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    print()
    root.print_indentation()
