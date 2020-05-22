#Submitted by thr3sh0ld using Counters
#learnt counters and dictionaries and params
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        dic = Counter(s)
        lis = []
        for key in sorted(dic,key=dic.get,reverse=True):
            for i in range(dic[key]):
                lis.append(key)
        return("".join(lis))
            