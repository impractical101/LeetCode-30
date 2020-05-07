class Solution:
    def firstUniqChar(self, s: str) -> int: #brute radicaf using dictionary simplified approach
        if len(s) == 0:
            return -1
        if len(s) == len(set(s)):
            return 0
        brute = {}
        for rand1 in s:
            if rand1 not in brute:
                brute[rand1] = 1
            else:
                brute[rand1] += 1
        for res, rand1 in enumerate(s):
            if brute[rand1] == 1:
                return res
        return -1
