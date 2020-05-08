class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if(len(coordinates))==2 :
            return True
        p1,p11 = coordinates[1]
        p2,p22 = coordinates[2]
        
        if p1==p2:
            for i in range(2,len(coordinates)):
                c = coordinates[i]
                if c[0] != p2:
                    return False
            return True
        a = (p22-p11)/(p2-p1)
        for i in range(len(coordinates)):
            c = coordinates[i]
            slope =0
            try:
                 slope = float(c[1]- p11)/float(c[0] -p1)
            except ZeroDivisionError:
                c = float('Inf')
            if slope!=a:
                return False 
            else: return True
           
