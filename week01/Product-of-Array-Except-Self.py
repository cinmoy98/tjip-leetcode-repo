# Problem Link : https://leetcode.com/problems/product-of-array-except-self/submissions/
# Problem Number : 238
# Problem Tag : Array
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 30/3/2022

# Approach 1,Time-complexity--> O(n), Space-Compllexity--> O(1) 
################################################################
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i=0
        mul = 1
        result=[]
        while(i<len(nums)):
            result.append(1)
            i=i+1
        for i in range(1,len(nums)):
            result[i]=result[i-1]*nums[i-1]
        i=i-1
        while(i>=0):
            mul=mul*nums[i+1]
            result[i]=result[i]*mul
            i=i-1
        return result