"""
145. 二叉树的后序遍历
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        h, c = root, None
        while stack:
            c = stack[-1]
            if c.left and h != c.left and h != c.right:  # c.children not printed
                stack.append(c.left)
            elif c.right and h != c.right:
                stack.append(c.right)
            else:
                h = stack.pop()
                res.append(h.val)
        return res

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack1 = [root]
        stack2 = []
        while stack1:
            r = stack1.pop()
            stack2.append(r)
            if r.left:
                stack1.append(r.left)
            if r.right:
                stack1.append(r.right)
        while stack2:
            node = stack2.pop()
            res.append(node.val)
        return res
