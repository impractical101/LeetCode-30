#Submitted by thr3sh0ld
#Simple bruteforcing. Think and code as you move along the matrice to find squares
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        r,c= len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    r1,c1= i,j
                    while r1<r and c1<c:
                        flag= False
                        for m in range(j,c1+1):
                            if matrix[r1][m] == 0:
                                flag =True
                                break
                        if not flag:
                            for n in range(i,r1+1):
                                if matrix[n][c1] ==0:
                                    flag = True
                                    break
                        if not flag:
                            ans+=1
                        else:
                            break
                        r1+=1
                        c1+=1
        return ans
        
    
    
