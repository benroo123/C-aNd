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


class AddTwoNums:
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
            return
        if listA.next is None and listB is None and car == 1:
            cur.next = ListNode(1)
            return

        add = listA.val + listB.val + car

        if add >= 10:
            car = 1
            add -= 10
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
    @staticmethod
    def trans(linked: ListNode):
        result = []
        while linked.next is not None:
            print(linked.val)
            result.append(linked.val)
            linked = linked.next
        return result

    def addTwoNumbers(self, listA: ListNode, listB: ListNode) -> ListNode:
        car = 0
        result = ListNode
        while listA.next is not None or car == 1:
            result1 = ListNode
            # result2 = ListNode
            car = 0
            add = listA.val + listB.val + car
            if add >= 10:
                car = 1
                add -= 10
            result1.val = add
            # result1.nextI = result2
            result.next = result1

        return result.next


if __name__ == "__main__":
    c = ListNode(7, None)
    b = ListNode(5, c)
    a = ListNode(3, b)

    g = ListNode(5, None)
    f = ListNode(3, g)
    e = ListNode(4, f)

    atn = AddTwoNums()
    atn.rec(e, a)
