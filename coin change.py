import sys

class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        self.coins = coins
        self.coins.sort()
        self.memo = {}
        ret = self.recursiveCoinChange(amount)
        return ret 
    
    
    def recursiveCoinChange(self, amount):
        
        if amount==0:
            return 0

        i=0
        n_coins_ls = []
        while i < len(self.coins) and amount >= self.coins[i]:
            remaining_amount = amount - self.coins[i]
            if remaining_amount not in self.memo.keys():
                self.memo[remaining_amount] = self.recursiveCoinChange(remaining_amount)
            n_coins = self.memo[remaining_amount]
            if n_coins != -1:
                n_coins_ls.append(n_coins + 1)
            i+=1


        return min(n_coins_ls) if n_coins_ls else -1
        

coins = [1,2,5]
amount = 11

op = Solution()
op.coinChange(coins, amount)

# Uses python3

if __name__ == '__main__':
    coins = [1,3,4]
    amount = int(sys.stdin.read())
    op = Solution()
    change = op.coinChange(coins, amount)
    print(change)