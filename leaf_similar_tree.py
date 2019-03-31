# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.value_sequence_1 = []
        self.value_sequence_2 = []
        self.leaf_finder(root1, self.value_sequence_1 )
        self.leaf_finder(root2, self.value_sequence_2 )
        
        if self.value_sequence_1 == self.value_sequence_2:
            return True
        return False

    def leaf_finder(self, node: TreeNode, sequence) -> None:
        if node.left:
            self.leaf_finder(node.left, sequence)
        if node.right:
            self.leaf_finder(node.right, sequence)
        if node.left is None and node.right is None:
            sequence.append(node.val)
