# Problem Link : https://leetcode.com/problems/longest-common-prefix/
# Problem Number : 14
# Problem Tag : String
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 16/4/2022

# Approach 1 (Bruitforce)
# Time-complexity--> O(N^2)
# Space-Compllexity--> O(1)
####################################################################
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ln = len(strs)
        len0 = len(strs[0])
        result = ""
        flag = 0
        for i in range(len0):
            cn = 0
            str_chk = strs[0][i]
            for s in strs:
                if i==(len(s)):
                    flag = 1
                    break
                if s[i]==str_chk:
                    cn=cn+1
                else:
                    break
            if cn==ln:
                result = result+str_chk
            else:
                break
            if flag==1:
                break
        return result

