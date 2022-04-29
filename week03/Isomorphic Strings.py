# Problem Link : https://leetcode.com/problems/isomorphic-strings/
# Problem Number : 205
# Problem Tag : Hash Map
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 28/04/2022

# Approach 1 --> Hashmap
# Time-complexity--> O(n), Space-Compllexity--> O(1) 
################################################################

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        cnt = collections.defaultdict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=t[i]
                if t[i] in cnt:
                    return False
                else:
                    cnt[t[i]]=1
            else:
                if t[i]==d[s[i]]:
                    continue
                else:
                    return False
        return True
                    