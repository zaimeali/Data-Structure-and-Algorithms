# https://leetcode.com/problems/add-two-numbers/

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

    i = 0
    while l2:
        if i < len(arr):
            arr[i] += l2.val
        else:
            arr.append(l2.val)
        l2 = l2.next
        i += 1

    print(arr)


def sol(l1, l2):
    num1 = ""
    while l1:
        num1 += str(l1.val)
        l1 = l1.next

    num2 = ""
    while l2:
        num2 += str(l2.val)
        l2 = l2.next

    num1 = int(num1)
    num2 = int(num2)
    res = str(num1 + num2)
    l3 = None
    for char in res:
        l3 = ListNode(char, l3)

    print(num1, num2)
    print(res)
    print_ll(l3)


def sol3(l1, l2):
    arr = []
    while l1:
        arr.append(l1.val)
        l1 = l1.next

    i = 0
    while l2:
        if i < len(arr):
            arr[i] += l2.val
        else:
            arr.append(l2.val)
        l2 = l2.next
        i += 1


if __name__ == '__main__':
    arr1 = [3, 4, 2]
    l1 = None
    for a in reversed(arr1):
        l1 = ListNode(a, l1)

    arr2 = [4, 6, 5]
    l2 = None
    for a in reversed(arr2):
        l2 = ListNode(a, l2)

    print_ll(l1)
    print_ll(l2)
    solution(l1, l2)
    sol(l1, l2)

    arr1 = [2, 4, 9]
    l1 = None
    for a in reversed(arr1):
        l1 = ListNode(a, l1)

    arr2 = [5, 6, 4, 9]
    l2 = None
    for a in reversed(arr2):
        l2 = ListNode(a, l2)

    print_ll(l1)
    print_ll(l2)
    solution(l1, l2)
    sol(l1, l2)
    sol3(l1, l2)
