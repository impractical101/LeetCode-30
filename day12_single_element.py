#submitted by thr3sh0ld 
#using counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        from collections import Counter

        c = Counter(nums)
        for i in c.elements():
            if c[i] == 1:
                return i
            else:
                i+=1
            
            
        
