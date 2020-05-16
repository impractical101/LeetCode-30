# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Submitted by thr3sh0ld
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        curr= head
        temp1 = head.next
        temp = head.next
        curr.next = curr.next.next
        curr= curr.next
        
        
        while curr and curr.next:
            temp.next = curr.next  #1
            temp = temp.next        #3
            if curr.next.next:
                curr.next = curr.next.next
                if curr.next:
                    curr= curr.next
            else:
                curr.next = temp1
                return head
        curr.next = temp1
        temp.next = None
        return head
    