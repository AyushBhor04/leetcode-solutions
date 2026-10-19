class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        bool_array=[]
        for candy in candies : 
            new = candy + extraCandies
            if(new >= max_candies):
                bool_array.append(True)
            else:
                bool_array.append(False)
        return bool_array