# Problem Link : https://leetcode.com/problems/valid-parentheses/
# Problem Number : 20
# Problem Tag : String
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 17/4/2022

# Approach 1 (Stack)
# Time-complexity--> O(N)
# Space-Compllexity--> O(N)
####################################################################
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        stack.append("")
        pair = {')':'(',']':'[', '}':'{'}
        for i in range(len(s)):
            if s[i] not in pair:
                stack.append(s[i])
            elif stack[-1]==pair[s[i]]:
                stack.pop()
            else:
                return False
        
        return True if len(stack)<=1 else False