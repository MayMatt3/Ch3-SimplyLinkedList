class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def split(head):
    fast = head
    slow = head

    while fast is not None and fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    temp = slow.next
    slow.next = None
    return temp


def merge(first, second):
    if first is None:
        return second
    if second is None:
        return first

    if first.data < second.data:
        first.next = merge(first.next, second)
        return first
    else:
        second.next = merge(first, second.next)
        return second


def MergeSort(head):
    if head is None or head.next is None:
        return head

    second = split(head)
    head = MergeSort(head)
    second = MergeSort(second)
    return merge(head, second)


def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


def average_evens(head):
    curr = head
    totalSum = 0
    count = 0

    while curr is not None:
        if curr.data % 2 == 0:
            totalSum += curr.data
            count += 1
        curr = curr.next

    if count == 0:
        return None
    else:
        return totalSum / count


def inputList():
    elements = [4, 2, 7, 1, 6, 3, 5]
    head = Node(elements[0])
    curr = head
    for i in range(1, len(elements)):
        new_node = Node(elements[i])
        curr.next = new_node
        curr = new_node
    return head


if __name__ == "__main__":
    head = inputList()
    print("Original List:")
    printList(head)
    head = MergeSort(head)
    print("\nSorted List:")
    printList(head)

    average = average_evens(head)
    print("\nAverage of even elements:", average)