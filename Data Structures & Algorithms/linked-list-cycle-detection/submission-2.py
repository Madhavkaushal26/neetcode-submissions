# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head

        d = []
        while curr:
            if curr.val in d:
                if curr.next == None or curr.next.val not in d:
                    curr = curr.next
                    continue
                return True
            d.append(curr.val)
            curr = curr.next

        return False 