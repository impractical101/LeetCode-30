#submitted by thr3sh0ld
#handling all the conditions in a same function
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def check(num):
            flag = 0
            if k == 0: 
                return num
            if len(num) == 1:
                return ['0']
            for i in range(1,len(num)):
                if num[i-1] > num[i]:
                    flag = 1 
                    break
            if not flag:
                del num[-1]
            else:
                del num[i-1]
            return num
            
        if len(num) == k:
            return "0"
        lis = list(num)
        while k !=0 :
            lis = check(lis)
            k -= 1
        return "".join(lis).lstrip("0") or "0"
            
                
