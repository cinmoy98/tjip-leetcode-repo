# Problem Link : https://leetcode.com/problems/minimum-window-substring/
# Problem Number : 76
# Problem Tag : String
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 21/04/2022

# Approach 1 (Two pointer )
# Time complexity --> O(M+N)
# Space Complexity --> O(1)
################################################################




class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        freqT = {}
        for char in t:
            if char in freqT:
                freqT[char]+=1
            else:
                freqT[char]=1
        L=0
        R=0
        cnt=len(t)
        minlen = 999999
        result = ""
        while(L<len(s)):
            if cnt>0 and R==len(s):
                break
            if R<len(s) and s[R] in freqT and cnt>0:
                freqT[s[R]]-=1
                if freqT[s[R]]>=0:
                    cnt-=1
                R+=1
            elif R<len(s) and s[R] not in freqT and cnt>0:
                R+=1
                
            if cnt<=0:
                if s[L] in freqT:
                    freqT[s[L]]+=1
                    if freqT[s[L]]>0:
                        cnt+=1
                if (R-L+1)<minlen:
                    minlen = R-L+1
                    result = s[L:R]
                L+=1
        return result