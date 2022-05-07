# Problem Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Problem Number : 3
# Problem Tag : String
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 16/4/2022

# Approach 1 (Two pointer)
# Time-complexity--> O(N)
# Space-Compllexity--> O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freqs = [0]*256
        sLength = len(s)
        L = 0
        R = 0
        cnt=0
        maxLength = 0
        while(R<sLength):
            freqs[ord(s[R])] += 1
            if freqs[ord(s[R])]>1:
                cnt+=1
            R=R+1
            while(cnt>0):
                freqs[ord(s[L])]-=1
                if freqs[ord(s[L])]==1:
                    cnt-=1
                L+=1
            maxLength=max(maxLength, R-L)
        return maxLength