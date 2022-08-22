# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        return self.InvertTree(root, None)
    
    def InvertTree(self, original, copied):
        if original is None:
            return
        
        copied = TreeNode()    
        copied.val = original.val

        copied.right = self.InvertTree(original.left, copied.right)
        copied.left = self.InvertTree(original.right, copied.left)
        
        return copied


