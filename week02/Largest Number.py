# Problem Link : https://leetcode.com/problems/largest-number/
# Problem Number : 179
# Problem Tag : String, Array
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 18/4/2022

# Approach 1 (Sorting converted integer)
################################################################

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums)==1:
            return str(nums[0])
        flag = 1
        num_str = []
        for num in nums:
            num_str.append(str(num))
        num_str.sort(reverse=True)
        
        
        while(flag==1):
            flag = 0
            result = ""
            for i in range(1,len(num_str)):
                if int(num_str[i]+num_str[i-1])>int(num_str[i-1]+num_str[i]):
                    num_str[i-1],num_str[i] = num_str[i],num_str[i-1]
                    flag = 1
                result+=num_str[i-1]
        return str(int(result+num_str[-1]))