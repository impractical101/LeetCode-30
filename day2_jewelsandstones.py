class Solution:
    count = 0 
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0 
        for i in S:
            count += 1 if i in J else 0
        return count
                           
                           
                           
                          
        
