class StockSpanner:

    def __init__(self):
        self.sol = [(0, float('inf'))]

    def next(self, res):
        x, y = self.sol[-1]
        if y > res:
            self.sol.append((1, res))
        elif y == res:
            self.sol.append((x + 1, res))            
        else:        
            t = 1
            while y <= res:
                t += x
                x, y = self.sol[0 - t]
            self.sol.append((t, res))
            
        return self.sol[-1][0]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)