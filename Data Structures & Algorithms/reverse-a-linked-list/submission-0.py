# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current = head
        values = []

        # Add all values to a list
        while current is not None:
            values.append(current.val)
            current = current.next
        # Read List in reverse, and update list
        i = len(values) - 1
        current = head
        while i >= 0 and current is not None:
            value = values[i]
            current.val = value
            current = current.next
            i -= 1
        return head