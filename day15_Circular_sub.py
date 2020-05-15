#Submitted by thr3sh0ld
#Circular array using array sign rotation tto handle case 2
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def max_kanade(a,size): 
            max_final = -maxsize - 1
            max_terminal = 0
            start = 0
            end = 0
            s = 0
            for i in range(0,size): 
                max_terminal += a[i] 
                if max_final < max_terminal: 
                    max_final = max_terminal 
                    start = s 
                    end = i 

                if max_terminal < 0: 
                    max_terminal = 0
                    s = i+1
            return max_final
        
        Max = max_kanade(A,len(A))
        cirl = 0
        for i in range(len(A)): # handling case 2
            cirl += A[i]
            A[i] = -A[i]
        cirl = cirl + max_kanade(A,len(A))
        if cirl > Max and cirl != 0:
            return cirl
        else:
            return Max
