# Problem Link : https://leetcode.com/problems/decode-string/
# Problem Number : 394
# Problem Tag : String
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 23/04/2022



# Approach 1 (Stack)(Got help from editorial)
# Time complexity --> O(N), N is max output length
# Space Complexity --> O(N)
################################################################

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [""]
        num = 0
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char=="[":
                stack.append(num)
                stack.append("")
                num=0
            elif char=="]":
                str1=stack.pop()
                str1=str1*stack.pop()
                str1=stack.pop()+str1
                stack.append(str1)
            else:
                stack[-1]+=char
        return stack[0]

