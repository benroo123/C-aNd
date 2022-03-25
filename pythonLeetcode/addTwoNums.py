# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
# reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as
# a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


class Solution:
    def rec(self, listA, listB, car=0):
        """
        :param listA:
        :param listB:
        :param car: the carry bit which is 0 at the beginning
        :return: return a linked list
        """
        cur = ListNode()
        if listA.next is None and listB is None and car == 0:
            cur.next = None
            return None
        if listA.next is None and listB is None and car == 1:
            return ListNode(1)

        add = listA.val + listB.val + car

        if add >= 10:
            car = 1
            add -= 10
        # set the value of the current node
        cur.val = add

        print(cur.val, cur.next)
        if listA.next is None:
            rep = ListNode()
            cur.next = self.rec(rep, listB.next, car)
        elif listB.next is None:
            rep = ListNode()
            cur.next = self.rec(listA.next, rep, car)
        else:
            cur.next = self.rec(listA.next, listB.next, car)
        # print(cur.val)
        return cur

    # a is none, b is none
    # a is none, b is not none
    # a is not none, b is none
    # a is not none, b is not none
    # Cannot just list four scenarios because the item after next one could be a lot. NOR JUST ONE
    class Solution:
        def addTwoNumbers(self, l1: ListNode, l2: ListNode, car=0) -> ListNode:
            current = ListNode()

            carry = 0
            sum = l1.val + l2.val + car
            if sum >= 10:
                carry = 1
                current.val = sum - 10
            else:
                current.val = sum

            if l1.next is None and l2.next is None and carry == 0:
                return current
            elif l1.next is None and l2.next is None and carry == 1:
                next = ListNode(1)
                current.next = next
                return current
            else:
                print(l1.val, l2.val, current.val)
                empty = ListNode()
                if l1.next is not None and l2.next is not None:
                    print("c1")
                    current.next = Solution.Solution(self, l1.next, l2.next, carry)
                elif l1.next is not None and l2.next is None:
                    print("c2")
                    current.next = Solution.Solution(self, l1.next, empty, carry)
                elif l2.next is not None and l1.next is None:
                    print("c3")
                    current.next = Solution.Solution(self, empty, l2.next, carry)
                return current


if __name__ == "__main__":
    c = ListNode(7, None)
    b = ListNode(5, c)
    a = ListNode(3, b)

    g = ListNode(5, None)
    f = ListNode(3, g)
    e = ListNode(4, f)

    atn = AddTwoNums()
    atn.addTwoNumbers(e, a)
