from logging.config import listen


class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        self.nums = nums
        self.memo = {}
        max_subsequence = 0
        for i in range(len(nums)):

            len_sub = self.find_LIS(i)
            if len_sub > max_subsequence:
                max_subsequence = len_sub

        
        return max_subsequence
                
    def find_LIS(self,idx):
        n1 = self.nums[idx]
        subsequence = set()
        for i, n2 in enumerate(self.nums[idx+1:]):
            if n2 > n1:
                subsequence.add(idx+1+i)
        if not subsequence or not self.nums:
            return 1

        max_subsequence = 0
        for i in subsequence:
            
            if i not in self.memo.keys():
                self.memo[i] = self.find_LIS(i)
            
            len_sub = self.memo[i]+1
            if len_sub > max_subsequence:
                max_subsequence = len_sub

        return max_subsequence
    
        
                    
                
nums = [0, 510, 9, 2, 5, 3, 7, 101, 18, 7, 7, 6]
op = Solution()
op.lengthOfLIS(nums)