# Problem Link : https://leetcode.com/problems/two-sum/
# Problem Number : 1
# Problem Tag : Array
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 30/3/2022

# Approach 1
################################################################
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,elmnt in enumerate(nums):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]