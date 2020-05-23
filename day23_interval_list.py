#Submitted by thr3sh0ld
#Find a valid interval first then do a max of the start values and min of the ends
class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Intervxl]') -> 'List[Intervxl]':
        x, y = 0, 0
        lis = []
        while x < len(A) and y < len(B):
            if A[x][1] < B[y][0]:
                x += 1
                continue
            elif A[x][0] > B[y][1]:
                y += 1
                continue
            L = max(A[x][0], B[y][0])
            R = min(A[x][1], B[y][1])
            lis.append([L, R])
            if A[x][1] > B[y][1]:
                y += 1
            else:
                y += 1
        return lis