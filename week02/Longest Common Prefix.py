# Problem Link : https://leetcode.com/problems/longest-common-prefix/
# Problem Number : 14
# Problem Tag : String
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 17/4/2022

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

# Approach 2 (Frequency counting)
# Time-complexity--> O(N)
# Space-Compllexity--> O(N)
####################################################################

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        freqs = {}
        output = []
        result = ""
        for s in strs:
            for i in range(len(s)):
                if s[i] not in freqs:
                    freqs[s[i]]={i:0}
                    
                if i not in freqs[s[i]]:
                    freqs[s[i]][i]=0
                
                freqs[s[i]][i] += 1
                
                if freqs[s[i]][i]==len(strs):
                    output.append((i,s[i]))
                    
        k=1
        if len(output)>=1 and output[0][0]==0:
            result=result+output[0][1]
        
        while(k<len(output)):
            if output[k][0]==output[k-1][0]+1:
                result=result+output[k][1]
            else:
                break
            k+=1
        
        return result
