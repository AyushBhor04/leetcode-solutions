class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = 0
        sum_list = []
        for num in nums:
            sum = sum + num
            sum_list.append(sum)
        return (sum_list)