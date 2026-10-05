class Solution:
    def socialNetwork(self, arr):
        n = len(arr) + 1
        res = []
        
        for i in range(2, n + 1):
            curr = i
            dist = 0
            reachable = []
            
            while curr > 1:
                curr = arr[curr - 2]
                dist += 1
                reachable.append((curr, dist))
            
            reachable.sort(key=lambda x: x[0])
            
            for j, k in reachable:
                res.append([i, j, k])
                
        return res