# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    @staticmethod
    def traverse(root: TreeNode, search: TreeNode, path: List[TreeNode]) -> List[TreeNode] | None:  
        if not root:
            return None

        path.append(root)
        if root.val == search.val:
            return path
        if root.left:
            left_path = Solution.traverse(root.left, search, path)
            if left_path:
                return left_path
        if root.right:
            right_path = Solution.traverse(root.right, search, path)
            if right_path:
                return right_path

        path.pop()
        return None

    @staticmethod
    def getValues(path: List[TreeNode]) -> List[int]:
        values = []
        for node in path:
            values.append(node.val)
        return values

    @staticmethod
    def getLowestCommon(p_path: List[TreeNode], q_path: List[TreeNode]) -> TreeNode:
        print(Solution.getValues(p_path or []))
        print(Solution.getValues(q_path or []))
        common = []
        lowest = None
        min = None
        for node in p_path:
            if node in q_path:
                common.append(node)
        return common[-1]

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root
        p_path = Solution.traverse(root, p, [])
        q_path = Solution.traverse(root, q, [])
        lowest = Solution.getLowestCommon(p_path or [], q_path or [])
        return lowest