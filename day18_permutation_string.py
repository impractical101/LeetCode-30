#Submitted by thr3sh0ld
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        fors1 = [ord(x) - ord('a') for x in s1]
        fors2 = [ord(x) - ord('a') for x in s2]

        comp = [0] * 26
        for x in fors1:
            comp[x] += 1

        window = [0] * 26
        for i, x in enumerate(fors2):
            window[x] += 1
            if i >= len(fors1):
                window[fors2[i - len(fors1)]] -= 1
            if window == comp:
                return True
        return False