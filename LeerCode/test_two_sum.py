class Solution:
    nums = [2, 7, 11, 15]
    def twoSum(self, nums: list[int], target: int) -> list[int]:
         seen = {}
         for i, num in enumerate(nums):
             if target - num in seen:
                 return([seen[target - num], i])
             elif num not in seen:
                 seen[num] = i
                