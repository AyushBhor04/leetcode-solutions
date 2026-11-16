class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        count = 2 
        while count > 0 :
            for i in nums:
                ans.append(i)
            count = count - 1
        return ans  