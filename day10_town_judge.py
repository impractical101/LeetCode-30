#submitted by thr3sh0ld
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        from collections import Counter
        count = Counter()
        mapper = set()
        if N ==1 and not trust:
            return 1 
        for i,j in trust: #each element of list of list 
            count[j] += 1
            mapper.add(i)
        for key in count:
            if count[key] == N-1 and key not in mapper:
                 return key
        return -1 

