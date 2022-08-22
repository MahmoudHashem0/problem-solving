# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        len_nums = len(nums)
        head = TreeNode()
        self.nums = nums
        self.func(head, 0, len_nums-1)
        return head
    
    def func(self, head, start, end):
        med = start + (end-start)//2
        val = self.nums[med]
        head.val = val

        if start < med:
            head.left = TreeNode()
            self.func(head.left, start, med-1)
        if end > med:
            head.right = TreeNode()
            self.func(head.right, med+1, end)
        return

nums = list(range(9))
op = Solution()
op.sortedArrayToBST(nums)