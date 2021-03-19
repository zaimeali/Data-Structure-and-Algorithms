# Custom Linked List
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def add(self, new):
        new.next = self.head
        self.head = new
    

link = LinkedList()
# elem = Node('Zaime')
# link.head = elem
# elem = Node('Faraz')
# link.head.next = elem
# elem = Node('Osama')
# link.head.next.next = elem
# elem = Node('Anas')
# link.head.next.next.next = elem

link.add(Node('Zaime'))
# link.show()
link.add(Node('Osama'))
link.show()

link.add(Node('Faraz'))
print()
link.show()