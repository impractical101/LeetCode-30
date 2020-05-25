#Submitted bythr3sh0ld using DP
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        mat = [[0] * (len(B)+1) for i in range(len(A)+1)]
        val = 0
        def maxi(r, c):
            return max(mat[r-1][c], mat[r][c-1])
        for x in range(len(A)):
            r = x + 1
            for y in range(len(B)):
                c = y + 1
                if A[x] == B[y]:
                    mat[r][c] = mat[r-1][c-1] + 1
                else:
                    mat[r][c] = maxi(r, c)
                if mat[r][c] > val:
                    val = mat[r][c]
        return val