class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        count = 2
        ans = [] 
        while(count):
            for i in nums :
                ans.append(i)
            count = count - 1
        return ans 