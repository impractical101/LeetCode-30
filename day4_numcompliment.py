class Solution:
    def findComplement(self, num: int) -> int:
        m = bin(num).replace("0b","") #easiest to find binary 
        ezzzz = len(m)
        m = "1" * ezzzz
        return int(m, 2) - num #given string to decimal with a base

"""
m =str(m)
        for i in range(0,len(m)):
            if(m[i]==0):
                m[i].replace('0','1')
            else:
                m[i].replace('1','0')
            
        return (int(m,2) - int(m))"""
               
"""
        
        def dtb(m : int):
            if(m > 1):  
                dtb(m//2)  
            return m%2
        ans = dtb(m)
        print(ans)"""
    

"""
if num > 1:
                dtob(num // 2)
            return num % 2
"""
    
