# -*- coding: utf-8 -*-
# @Time : 2022/11/7 22:21
# @Author : hehaiyang
# @File : day1.py
# @Project : learn
# @Function :
# Definition for singly-linked list.

# ------------------------------------两数相加----------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        # 初始化链表
        head = tree = ListNode()

        val = tmp = 0
        # 当三者有一个不为空时继续循环
        while tmp or l1 or l2:
            val = tmp
            if l1:
                val = l1.val + val
                l1 = l1.next
            if l2:
                val = l2.val + val
                l2 = l2.next

            tmp = val // 10
            val = val % 10

            # 实现链表的连接
            tree.next = ListNode(val)
            tree = tree.next

        return head.next


l11 = ListNode(2)
l12 = ListNode(4, l11)
l13 = ListNode(1, l12)
l21 = ListNode(5)
l22 = ListNode(6, l21)
l23 = ListNode(4, l22)
print(Solution().addTwoNumbers(l13, l23))
