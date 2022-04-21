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