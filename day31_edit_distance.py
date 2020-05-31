#Submitted by thr3sh0ld
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not len(word1) or not len(word2):
            return len(word1)+len(word2)
        if len(word1) < len(word2):
           word1, word2 = word2, word1
        len1, len2 = len(word1), len(word2)
        dp= [0]*(len1+1)
        rev = [len2-j for j in range(len1+1)]
        for i in range(len1-1, -1, -1):
            for j in range(len1, len2-1,-1):
                dp[j] = len1-i
            for j in range(len2-1, -1, -1):
                dp[j] = min(rev[j+1] + [1,0][word1[i]==word2[j]],1+min(dp[j+1], rev[j]))
            dp, rev = [0]*(len1+1), dp
        return rev[0]