# Problem Link : https://leetcode.com/problems/roman-to-integer/
# Problem Number : 13
# Problem Tag : Hash Map
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 29/04/2022

# Approach 1 --> Hashmap
# Time-complexity--> O(n), Space-Compllexity--> O(1)
################################################################
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        i=0
        num = 0
        while(i<len(s)-1):
            if s[i]=="I":
                if s[i+1]=="V" or s[i+1]=="X":
                    num = num + (d[s[i+1]]-d[s[i]])
                    i=i+2
                else:
                    num = num + d[s[i]]
                    i=i+1
            elif s[i]=="X":
                if s[i+1]=="L" or s[i+1]=="C":
                    num = num + (d[s[i+1]]-d[s[i]])
                    i=i+2
                else:
                    num = num + d[s[i]]
                    i=i+1
            elif s[i]=="C":
                if s[i+1]=="D" or s[i+1]=="M":
                    num = num + (d[s[i+1]]-d[s[i]])
                    i=i+2
                else:
                    num = num + d[s[i]]
                    i=i+1
            else:
                num = num+d[s[i]]
                i=i+1
        if i==(len(s)-1):
            num = num + d[s[i]]
        return num