"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]



 

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        stack1 = [root]
        stack2 = []
        target = []
        cache = {root.val: None}
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.val in (p.val, q.val):
                target.append(node)
            if len(target) == 2:
                break
            if node.left:
                stack1.append(node.left)
                cache[node.left.val] = node
            if node.right:
                stack1.append(node.right)
                cache[node.right.val] = node
        visited = set()
        t1, t2 = target
        while t1:
            visited.add(t1.val)
            t1 = cache[t1.val]
        while t2:
            if t2.val in visited:
                return t2
            t2 = cache[t2.val]

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {}

        def dfs(node: 'TreeNode'):
            nonlocal parent
            if not node:
                return
            if node.left:
                parent[node.left.val] = node
                dfs(node.left)
            if node.right:
                parent[node.right.val] = node
                dfs(node.right)

        visited = set()
        dfs(root)
        while p:
            visited.add(p.val)
            p = parent[p.val]
        while q:
            if q.val in visited:
                return q
            q = parent[q.val]

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        common_parent = None

        def post_find(node: 'TreeNode'):
            nonlocal common_parent
            if not node:
                return False
            left = post_find(node.left)
            right = post_find(node.right)
            if left and right:
                common_parent = node
                return True
            if node.val in (p.val, q.val):
                if left or right:
                    common_parent = node
                return True
            return left or right
        post_find(root)
        return common_parent

