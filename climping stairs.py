class Solution:
    def climbStairs(self, n: int) -> int:
        self.n = n
        self.memo = {}
        count = 1
        i=1
        while i*2<=n:
            count+=self.func(0, i*2)
            i+=1
        return count
    
    def func(self, start=0, step=2):
        if step == 2:
            # n = self.n-start-3
            # tmp = (n/2)*(n+1)
            count = self.n - start -1
            return count

            # return self.n-i-1 # just for simplicity but this is wrong
        
        i = start+2
        count = 0
        while i < self.n:
            if ((i, step-2)) not in self.memo.keys():
                self.memo[(i, step-2)] = self.func(i, step-2)
            count+=self.memo[(i, step-2)]
            i+=1
        return count

op = Solution()

print(op.climbStairs(45))