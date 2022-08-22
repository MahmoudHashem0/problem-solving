# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        pass

    
    def isSame(self, p, q):
        
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        if p.val != q.val:
            return False
        
        
        l = self.isSame(p.left, q.left)
        r = self.isSame(p.right, q.right)

        if l and r:
            return True


