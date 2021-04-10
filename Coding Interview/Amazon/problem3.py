# 3. Merge two sorted linked lists

# Given two sorted linked lists, merge them so that the resulting linked list is also sorted.

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self._count = 0

    def get_count(self):
        return self._count

    def insert_at_last(self, data):
        self._count += 1
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print_list(self):
        if self.head is None:
            print('Empty List')
            return

        itr = self.head
        print("Head", end=" -> ")
        while itr:
            print(itr.value, end=" -> ")
            itr = itr.next
        print("Null")


def merge_sorted(head1, head2):
    merge_list = []
    while head1:
        merge_list.append(head1.value)
        head1 = head1.next

    while head2:
        merge_list.append(head2.value)
        head2 = head2.next

    merge_list = sorted(merge_list)
    ll = LinkedList()
    for i in merge_list:
        ll.insert_at_last(i)

    return ll


if __name__ == "__main__":
    list1 = LinkedList()
    list1.insert_at_last(4)
    list1.insert_at_last(8)
    list1.insert_at_last(15)
    list1.insert_at_last(19)

    list1.print_list()

    list2 = LinkedList()
    list2.insert_at_last(7)
    list2.insert_at_last(9)
    list2.insert_at_last(10)
    list2.insert_at_last(16)

    list2.print_list()

    new_list = merge_sorted(list1.head, list2.head)

    print(new_list.print_list())
