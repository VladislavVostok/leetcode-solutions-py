'''
Task complexity: medium

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
dd the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    |-----|       |-----|       |-----|
    |  2  |------>|  4  |------>|  3  |
    |-----|       |-----|       |-----|

    +             +             +

    |-----|       |-----|       |-----|
    |  5  |------>|  6  |------>|  4  |
    |-----|       |-----|       |-----|

    =             =             =

    |-----|       |-----|       |-----|
    |  7  |------>|  0  |------>|  8  |
    |-----|       |-----|       |-----|

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

'''

class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2:ListNode) -> ListNode:

    head = ListNode(0)
    temp_node = head
    sum_nodes, add_one = (0, 0)

    while l1 != None or l2 != None or add_one != 0:
        val_l1 = l1.val if l1 else 0
        val_l2 = l2.val if l2 else 0

        sum_nodes = val_l1 + val_l2 + add_one
        temp_node.val = sum_nodes % 10
        add_one = sum_nodes // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        if not (l1 != None or l2 != None or add_one != 0): return head
        new_node = ListNode(0)
        temp_node.next = new_node
        temp_node = temp_node.next


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    res = addTwoNumbers(l1, l2)
    print()
        
        

    


