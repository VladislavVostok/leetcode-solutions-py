# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode(0)
        cur = res_head
        add_one = 0
        while l1 != None or l2 != None or add_one !=0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum_ = l1_val + l2_val + add_one
            add_one = sum_ // 10
            new_node = ListNode(sum_ % 10)
            cur.next = new_node
            cur = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res_head.next

if __name__ == '__main__':
    s = Solution()
    print(s.addTwoNumbers(l1=[1,2,3], l2=[3,2,1]))










