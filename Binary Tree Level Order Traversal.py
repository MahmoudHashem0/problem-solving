# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        self.answer = []
        self.levels = set()
        self.mylevelOrder(root, 0)
        return self.answer
        
    def mylevelOrder(self, root, i):
        if root is None:
            return
        
        if i not in self.levels:
            self.answer.append([])
            self.answer[-1].append(root.val)
            self.levels.add(i)
        else:
            self.answer[i].append(root.val)
        
        self.mylevelOrder(root.left, i+1)
        self.mylevelOrder(root.right, i+1)
        


