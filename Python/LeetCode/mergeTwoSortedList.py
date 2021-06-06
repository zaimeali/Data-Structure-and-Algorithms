# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_ll(ll):
    while ll:
        print(ll.val)
        ll = ll.next


def solution(l1, l2):
    arr = []
    while l1:
        arr.append(l1.val)
        l1 = l1.next
    while l2:
        arr.append(l2.val)
        l2 = l2.next

    l3 = None
    for a in reversed(sorted(arr)):
        l3 = ListNode(a, l3)
    return l3


if __name__ == '__main__':
    arr1 = [1, 2, 4]
    l1 = None
    for a in reversed(arr1):
        l1 = ListNode(a, l1)

    arr2 = [1, 3, 4]
    l2 = None
    for a in reversed(arr2):
        l2 = ListNode(a, l2)

    print_ll(l1)
    print("")
    print_ll(l2)
    print("")
    print(print_ll(solution(l1, l2)))
