class Solution:
    import math
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0: return False
        newNum = int(num**(0.5))
        return newNum**2==num
        
"""
#a very unique approach 
if num<0:
            return False
        x,i=0,1
        while x<num:
            x+=i
            i+=2
        return x==num
"""
