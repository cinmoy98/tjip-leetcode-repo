# Problem Link : https://leetcode.com/problems/majority-element/
# Problem Number : 169
# Problem Tag : Array
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 30/3/2022

# Approach 1,Time-complexity--> O(nlog(n)), Space-Compllexity--> O(1) 
################################################################
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        mx = 1
        for i in range(0,len(nums)):
            if i==(len(nums)-1):
                break
            if nums[i]==nums[i+1]:
                mx=mx+1
            else:
                if mx>(len(nums)/2):
                    return nums[i]
                mx = 1
        return nums[i]