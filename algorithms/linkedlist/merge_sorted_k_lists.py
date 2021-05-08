"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""


from heapq import heappop, heapreplace, heapify
from queue import PriorityQueue
import heapq

# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_lists(lists):
    head = Node(None)
    curr = head
    h = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(h, (lists[i].val, i))
            lists[i] = lists[i].next

    while h:
        val, i = heapq.heappop(h)
        curr.next = Node(val)
        curr = curr.next
        if lists[i]:
            heapq.heappush(h, (lists[i].val, i))
            lists[i] = lists[i].next

    return head.next




"""
I think my code's complexity is also O(nlogk) and not using heap or priority queue,
n means the total elements and k means the size of list.

The mergeTwoLists function in my code comes from the problem Merge Two Sorted Lists
whose complexity obviously is O(n), n is the sum of length of l1 and l2.

To put it simpler, assume the k is 2^x, So the progress of combination is like a full binary tree,
from bottom to top. So on every level of tree, the combination complexity is n,
because every level have all n numbers without repetition.
The level of tree is x, ie log k. So the complexity is O(n log k).

for example, 8 ListNode, and the length of every ListNode is x1, x2,
x3, x4, x5, x6, x7, x8, total is n.

on level 3: x1+x2, x3+x4, x5+x6, x7+x8 sum: n

on level 2: x1+x2+x3+x4, x5+x6+x7+x8 sum: n

on level 1: x1+x2+x3+x4+x5+x6+x7+x8 sum: n
"""
