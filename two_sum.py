class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i, n1 in enumerate(nums):
            for j , n2 in enumerate(nums):
                if n1+n2 == target and i!=j:
                    return [i,j]


nums = [3,2,4]
target = 6
op = Solution()
op.twoSum(nums, target)