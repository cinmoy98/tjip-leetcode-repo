# Problem Link : https://leetcode.com/problems/string-to-integer-atoi/
# Problem Number : 08
# Problem Tag : String
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 22/04/2022

# Approach 1
# Time complexity --> O(N)
# Space Complexity --> O(1)
################################################################

class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        leading = True
        sign = True
        for i in range(len(s)):
            if s[i]==" " and leading==True:
                continue
            if leading==True and (s[i]=="-" or s[i]=="+") and (i+1)<len(s) and (ord(s[i+1])>=48 and ord(s[i+1])<=57):
                if s[i]=="-":
                    sign=False
                continue
            if ord(s[i])<48 or ord(s[i])>57:
                break
            num =(num*10)+(ord(s[i])-48)
            leading = False
        if sign==False:
            num = -num
            if num<-2147483648:
                num=-2147483648
        else:
            if num>2147483647:
                num = 2147483647
        return num