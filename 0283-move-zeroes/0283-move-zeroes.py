class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        # Fill the remaining positions with 0
        while k < len(nums):
            nums[k] = 0
            k += 1