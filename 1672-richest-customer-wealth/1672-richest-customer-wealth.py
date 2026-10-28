class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for i in accounts :
            sum = 0
            for j in i : 
                sum = sum + j

            if(max_wealth < sum):
                max_wealth = sum

        return max_wealth