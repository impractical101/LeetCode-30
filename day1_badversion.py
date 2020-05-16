#using bseearch and reducing time complex.
class Solution:
    def firstBadVersion(self, n):
        left,right = 1,n
        while right > left:
            middle = (left+right)//2
            if isBadVersion(middle): right = middle
            else: left = middle + 1
        return left
