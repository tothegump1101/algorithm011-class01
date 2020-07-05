"""
589. N叉树的前序遍历
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :

返回其前序遍历: [1,3,5,6,2,4]。

说明: 递归法很简单，你可以使用迭代法完成此题吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            for c in reversed(node.children):
                stack.append(c)
            res.append(node.val)
        return res

    def preorder1(self, root: 'Node') -> List[int]:
        res = []

        def trace(r: 'Node'):
            if not r:
                return
            res.append(r.val)
            for child in r.children:
                trace(child)

        trace(root)
        return res
