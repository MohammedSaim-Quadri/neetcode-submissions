class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [amount + 1] * (amount + 1)

        table[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a-c >= 0:
                    table[a] = min(table[a], 1+table[a-c])
        
        return table[amount] if table[amount] != amount+1 else -1