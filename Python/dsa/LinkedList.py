class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.__count = 0

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        self.__count += 1

    def print_list(self):
        if self.head is None:
            print('Empty List')
            return
        
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    def insert_at_last(self, data):
        self.__count += 1
        if(self.head is None):
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def get_count(self):
        return self.__count

    def remove_at(self, index):
        if index < 0 or index >= self.__count:
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_at(self, data, index):
        if index < 0 or index >= self.__count:
            raise Exception('Invalid Index')

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(10)
    ll.insert_at_begining(20)
    ll.insert_at_begining(30)
    ll.insert_at_last(40)

    ll.print_list()
    print("Count of LinkedList is: ", ll.get_count())


    # ll.remove_at(10)
    ll.remove_at(2)
    ll.print_list()

    print("\n")

    ll.insert_at(50, 0)
    ll.print_list()

    print("\n")

    ll.insert_at(60, 2)
    ll.print_list()