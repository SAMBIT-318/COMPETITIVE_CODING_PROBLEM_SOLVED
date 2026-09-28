import math

class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        # code here
        n = len(arr)
        tree = [0] * (4 * n)

        def build(node, start, end):
            if start == end:
                tree[node] = arr[start]
            else:
                mid = (start + end) // 2
                build(2 * node + 1, start, mid)
                build(2 * node + 2, mid + 1, end)

                tree[node] = math.gcd(tree[2 * node + 1], tree[2 * node + 2])


        def update(node, start, end, idx, val):
            if start == end:
                arr[idx] = val
                tree[node] = val
            else:
                mid = (start + end) // 2
                if start <= idx <= mid:
                    update(2 * node + 1, start, mid, idx, val)
                else:
                    update(2 * node + 2, mid + 1, end, idx, val)

                tree[node] = math.gcd(tree[2 * node + 1], tree[2 * node + 2])
                
        def query(node, start, end, l, r):

            if r < start or end < l:
                return 0 
            if l <= start and end <= r:
                return tree[node]
                
            mid = (start + end) // 2
            left_gcd = query(2 * node + 1, start, mid, l, r)
            right_gcd = query(2 * node + 2, mid + 1, end, l, r)
            return math.gcd(left_gcd, right_gcd)
        build(0, 0, n - 1)
        result = []
        for q in queries:
            if q[0] == 0:  
                l, r = q[1], q[2]
                result.append(query(0, 0, n - 1, l, r))
            elif q[0] == 1: 
                idx, val = q[1], q[2]
                update(0, 0, n - 1, idx, val)

        return result