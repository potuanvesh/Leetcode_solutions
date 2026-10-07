# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        temp=head
        count=0
        while temp:
            temp=temp.next
            count=count+1
        mid_value=count//2
        temp=head
        for _ in range(mid_value):
            temp=temp.next
        return temp
        