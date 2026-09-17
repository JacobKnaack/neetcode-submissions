# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return
        merged = ListNode()
        current1 = list1
        current2 = list2
        currentMerged = merged
        while current1 is not None and current2 is not None:
            if current1.val < current2.val:
                currentMerged.val = current1.val
                current1 = current1.next
            else:
                currentMerged.val = current2.val
                current2 = current2.next
            currentMerged.next = ListNode()
            currentMerged = currentMerged.next
        while current1 is not None:
            currentMerged.val = current1.val
            if current1.next is not None:
                currentMerged.next = ListNode()
                currentMerged = currentMerged.next
            current1 = current1.next
        while current2 is not None:
            currentMerged.val = current2.val
            if current2.next is not None:
                currentMerged.next = ListNode()
                currentMerged = currentMerged.next
            current2 = current2.next

        return merged