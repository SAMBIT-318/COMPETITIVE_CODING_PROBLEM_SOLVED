class Solution:
    def longestPath(self, s, edges):
        # code here
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        order = [0]
        parent = [-1] * n
        i = 0
        while i < len(order):
            u = order[i]
            i += 1
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        R = [0] * n
        B = [0] * n
        RB = [0] * n
        BR = [0] * n
        ans = 1
        for u in reversed(order):
            max_val1 = 0
            max_val2 = 0

            for v in adj[u]:
                if v == parent[u]: 
                    continue
                if s[u] == 'R':
                    v1 = R[v]
                    v2 = max(RB[v], B[v])
                else:
                    v1 = B[v]
                    v2 = max(BR[v], R[v])
                ans = max(ans, max_val1 + 1 + v2, v1 + 1 + max_val2)
                max_val1 = max(max_val1, v1)
                max_val2 = max(max_val2, v2)
            if s[u] == 'R':
                R[u] = 1 + max_val1
                RB[u] = 1 + max_val2
                ans = max(ans, R[u], RB[u])
            else:
                B[u] = 1 + max_val1
                BR[u] = 1 + max_val2
                ans = max(ans, B[u], BR[u])

        return ans