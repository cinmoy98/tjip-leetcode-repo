# Problem Link : https://leetcode.com/problems/implement-strstr/
# Problem Number : 28
# Problem Tag : String Hashing
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 16/4/2022

# Approach 1 (Bruitforce approach)
# Time-complexity--> O(H*N), H=len(haystack), N=len(needle)
# Space-Compllexity--> O(1)
################################################################
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ln = len(needle)
        lh = len(haystack)
        if ln>lh:return -1
        flag = 0
        for i in range (lh):
            if haystack[i]==needle[0]:
                for j in range(ln):
                    if i<lh and haystack[i]==needle[j]:
                        flag=1
                        i=i+1
                    else:
                        flag=0
                        break
                if flag==1:
                    return i-ln
        if flag==0:
            return -1

# Approach 2 (Hashing)
# Time-complexity--> O(H), H=len(haystack)
# Space-Compllexity--> O(H)
################################################################

class Solution:
    def pre_process(self, haystack, needle):
        self.haystackPrefixHash[0] = ord(haystack[0])
        for i in range(1,len(haystack)):
            self.haystackPrefixHash[i] = (self.haystackPrefixHash[i-1] * self.base)%self.MOD
            self.haystackPrefixHash[i] = self.haystackPrefixHash[i] + ord(haystack[i])
            self.power[i] = (self.power[i-1]*self.base)%self.MOD
            #print(self.power)
        for c in needle:
                self.needleHash = ((self.needleHash * self.base) + ord(c)) % self.MOD
        #print(self.haystackPrefixHash)
        #print(self.needleHash)
    def getRangeHash(self,l,r):
        if l==0:
            to_be_sub = 0 
        else:
            to_be_sub = self.haystackPrefixHash[l-1] * self.power[r-l+1]
        #print(self.haystackPrefixHash[l-1])
        #print(self.power[r-l+1])
        return (self.haystackPrefixHash[r]-to_be_sub+self.MOD)%self.MOD
    
    def strStr(self, haystack: str, needle: str) -> int:
        self.MOD = 1000000007
        self.base = 29
        lh = len(haystack)
        ln = len(needle)
        self.haystackPrefixHash = [0]*lh
        self.needleHash = 0
        self.power = [1]*lh
        
        self.pre_process(haystack, needle)
        for i in range(lh-ln+1):
            if self.getRangeHash(i, i+ln-1)==self.needleHash:
                return i
        return -1