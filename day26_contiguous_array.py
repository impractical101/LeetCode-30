#Submitted by thr3sh0ld
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        check = {0:-1}
        rem, maxi = 0, 0
        for i,x in enumerate(nums):
            rem = rem - 1 if x == 0 else rem + 1
            if rem in check:
                maxi = max(maxi, i-check[rem])
            else:
                check[rem] = i
        return maxi
