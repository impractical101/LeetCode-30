#Submitted by thr3sh0ld using DFS concept
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        temp = defaultdict(list)
        for i, j in dislikes:
            temp[i].append(j)
            temp[j].append(i)
        
        temp1 = [None]*(N+1)
        def find(x, y):
            if temp1[x] == None:
                temp1[x] = y
                return all(find(neighbor, not y) for neighbor in temp[x])
            else:
                return temp1[x] == y
            
        for i in range(1,N+1):
            if temp1[i] == None and find(i, True) == False:
                return False
        return True