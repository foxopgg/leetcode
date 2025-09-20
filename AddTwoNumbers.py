class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        current = result
        carry = 0
        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            Sum = l1Val + l2Val + carry
            carry = Sum // 10
            current.next = ListNode(Sum % 10)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next