#Submitted by thr3sh0ld 
#If a num is even then it hold the n/2 np of 1's and in case of odd it has n/2 +1 no pf 1's 
#To avoid division error in Python3 as it returns true division i.e. float, complile in python2 or handle the division error.I chose python2
class Solution:
    def countBits(self, num):
        bits = [0] * (num + 1)
        for i in range(num+1):
            if i % 2 == 0: # even
                bits[i] = bits[i/2]
            else: # odd
                bits[i] = bits[i//2] + 1
        return bits
        
        