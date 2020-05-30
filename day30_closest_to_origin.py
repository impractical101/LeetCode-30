#Submitted by thr3sh0ld 
#Using max heap and popping the first element i.e. the minimum distance
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K >= len(points): 
            return points
        
        maxii = [(-float('inf'), [0,0]) for _ in range(K)]
        
        for i in points:
            distance = i[0]**2 + i[1]**2
            heapq.heappush(maxii, (-distance, i))
            heapq.heappop(maxii)
            
        return [i[1] for i in maxii]