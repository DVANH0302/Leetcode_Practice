from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#           self.val = val
#         self.next = next

class Solution:
    @staticmethod        
    def findTail(node, k):
        if not node:
            return None
        size = 1
        while size < k:
            if node.next:
                node = node.next
                size += 1
            else:
                break
        
        if size == k:
            return node
        else:
            return None
        
    @staticmethod
    def reverseK(prev_head, head, tail):
        # tail_next = tail.next
        if prev_head: 
            prev_head.next = tail

        # restructuring the k list:
        l = head
        m = head.next
        r = head.next.next   
        l.next = None 
        while m != tail:
            m.next = l
            l = m 
            m  = r
            if r: 
                r = r.next
        
        head.next = tail.next
        tail.next = l

        return head, head.next
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        temp = head
        prev_head = None
        result_head = None
        while True:
            cur_tail = Solution.findTail(temp, k)

            if not result_head:
                result_head = cur_tail
            if cur_tail:
                prev_head, temp = Solution.reverseK(prev_head, temp, cur_tail)
            else:
                break
        return result_head

a = ListNode(1)
b = ListNode(2)
a.next = b 

s = Solution()
result = s.reverseKGroup(a, 2)

print(result.val, result.next.val)