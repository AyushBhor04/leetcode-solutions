class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        smaller_than_array = []
        for num in nums :
            count = 0 
            max = num 
            for j in nums : 
                if( max > j ):
                    count = count + 1
            smaller_than_array.append(count)
        return smaller_than_array 