# Problem Link : https://leetcode.com/problems/valid-anagram/submissions/
# Problem Number : 242
# Problem Tag : String
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 17/4/2022

# Approach 1 (Frequency count)
# Time-complexity--> O(N)
# Space-Compllexity--> O(1)
################################################################

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = [0]*256
        for char in s:
            sFreq[ord(char)]+=1
        
        for char in t:
            sFreq[ord(char)]-=1
        
        for freq in sFreq:
            if freq!=0:
                return False
        return True