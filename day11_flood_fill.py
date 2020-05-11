# recursive submitted by thr3sh0ld
class Solution:
    def floodFill(self,image,sr,sc,newColor):
        front, back, startCol= len(image), len(image[0]), image[sr][sc]
        if startCol == newColor:
            return image
        
        def floodf(r, c):
            if image[r][c] == startCol:
                image[r][c] = newColor
                if r+1 < front: floodf(r+1, c)
                if r-1 >= 0:  floodf(r-1, c)
                if c+1 < back:floodf(r, c+1)
                if c-1 >= 0 : floodf(r, c-1)
                    
        floodf(sr,sc)
        return image
        
            
        
