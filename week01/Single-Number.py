# Problem Link : https://leetcode.com/problems/single-number/
# Problem Number : 136
# Problem Tag : Array, BitWise Operation
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 02/04/2022

# Approach 1 --> BitWise Operation --> X-OR
# Time-complexity--> O(n), Space-Compllexity--> O(1) 
################################################################

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for elmnt in nums:
            result = result ^ elmnt
        return result