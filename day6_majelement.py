class Solution:
    def majorityElement(self, num: List[int]) -> int:
        dic = list(set(num))
        for i in dic:
            c = [val for val in sorted(num) if val == i]
            if len(c) > (len(num)/2):
                return i
                break
