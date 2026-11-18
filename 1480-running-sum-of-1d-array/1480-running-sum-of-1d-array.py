class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = 0 
        sum_of_list=[]
        for num in nums :
            sum = sum + num 
            sum_of_list.append(sum)
        return sum_of_list