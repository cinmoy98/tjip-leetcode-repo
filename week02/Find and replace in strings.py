# Problem Link : https://leetcode.com/problems/find-and-replace-in-string/
# Problem Number : 833
# Problem Tag : String
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 19/04/2022

# Approach 1 (Using flag)
# Time complexity --> O(N)
# Space Complexity --> O(N)
################################################################
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        freq_arr = [0]*len(s)
        result = ""
        for i in range(len(indices)):
            if s[indices[i]:indices[i]+len(sources[i])]==sources[i]:
                freq_arr[indices[i]] = i+1
        i=0
        while(i<len(s)):
            if freq_arr[i]!=0:
                result+=targets[freq_arr[i]-1]
                i = i + len(sources[freq_arr[i]-1])
            else:
                result+=s[i]
                i+=1
        return result