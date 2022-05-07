# Problem Link : https://leetcode.com/problems/group-anagrams/
# Problem Number : 49
# Problem Tag : String
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 18/4/2022


# Approach 1 (Frequency count) Got hint😥
# Time-complexity--> O(N*M) : len(strs)=N , len(strs[i])=M
# Space-Compllexity--> O(1)
################################################################
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        ans = collections.defaultdict(list)
        for s in strs:
            freqArr = [0]*26
            for char in s:
                freqArr[ord(char)-97]+=1
            ans[tuple(freqArr)].append(s)
        return ans.values()



# Approach 2 (Frequency count)
# Time-complexity--> O(N)
# Space-Compllexity--> O(N)
################################################################
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        freqs = {}
        for i in range(len(strs)):
            if strs[i] == "":
                strs[i] = "0"
            ln = len(strs[i])
            for char in strs[i]:
                if char not in freqs:
                    freqs[char] = []
                    freqs[char].append((i,ln))
                else:
                    freqs[char].append((i,ln))
        cat = [0]*len(strs)
        rslt_arr = []
        for i in range(len(strs)):
            rslt_arr.append([])
        cnt = 0
        for key,value in freqs.items():
            flag = 0
            for char_freq in value:
                cat[char_freq[0]]+=1
                if cat[char_freq[0]]==char_freq[1]:
                    rslt_arr[cnt].append(char_freq[0])
                    cat[char_freq[0]] = 0
                    flag=1
            if flag==1:
                cnt+=1
        output = []
        i=0
        cnt=0
        for cats in rslt_arr:
            output.append([])
            for word in cats:
                if strs[word]=="0":
                    output[i].append("")
                else:
                    output[i].append(strs[word])
                cnt+=1
            i+=1
            if cnt>=len(strs):
                break
        return output