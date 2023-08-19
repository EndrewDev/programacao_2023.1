class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         seen = {}
         for i, num in enumerate(nums):
             if target - num in seen:
                 return([seen[target - num], i])
             elif num not in seen:
                 seen[num] = i

nums = [2, 7, 11, 15]