from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = tail = ListNode()
    while True:
        try:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next

            tail = tail.next
        except AttributeError:
            break

    if list1 is None:
        tail.next = list2
    else:
        tail.next = list1

    return head.next
