# Problem Link : https://leetcode.com/problems/number-of-matching-subsequences/
# Problem Number : 792
# Problem Tag : String
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 23/04/2022

# Approach 2 (Occurrence count and binary search)(Used editorial😥)
# Time complexity --> O(MlogN)
# Space Complexity --> O(N)
################################################################

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ocur_indx = defaultdict(list)
        for i,c in enumerate(s):
            ocur_indx[c].append(i)
        
        def issubseq(word):
            min_pos = -1
            for char in word:
                if ocur_indx[char]:
                    indx = bisect.bisect_right(ocur_indx[char], min_pos)
                    if indx == len(ocur_indx[char]):
                        return False
                    min_pos = ocur_indx[char][indx]
                else:
                    return False
            return True
        
        
        
        cnt = 0
        for word in words:
            if issubseq(word):
                cnt+=1
        return cnt







#Approach 1(Occurrence,no bin search)
# Time complexity --> O(M*N)
# Space Complexity --> O(N)
#####################################################################################
from collections import defaultdict
s = "bacinmoydass"
words = ["aass","cidaa","cindoy","moyda","ass", "aioy", "cibd"]
# s = "abcde"
# words = ["a","bb","acd","ace"]

ocr_dict = defaultdict(list)
for i in range(len(s)):
    ocr_dict[s[i]].append(i)
cnt = 0
for word in words:
    word_freq = [-1]*26
    minimum = -1
    flag = 0
    k=0
    while(k<len(s)):
        for i in range(len(word)):
            word_freq[ord(word[i])-97]+=1
            if word[i] not in ocr_dict or len(ocr_dict[word[i]])<=word_freq[ord(word[i])-97]:
                flag=0
                break
            elif ocr_dict[word[i]][word_freq[ord(word[i])-97]] > minimum:
                minimum = ocr_dict[word[i]][word_freq[ord(word[i])-97]]
                print(ocr_dict[word[i]][word_freq[ord(word[i])-97]])
                flag = 1
            else:
                flag = 0
                break
            print(word_freq)
        if flag==1:
            print(word+" is a subsequence")
            cnt+=1
            break
        k+=1
    print("count"+str(cnt))
print(cnt)