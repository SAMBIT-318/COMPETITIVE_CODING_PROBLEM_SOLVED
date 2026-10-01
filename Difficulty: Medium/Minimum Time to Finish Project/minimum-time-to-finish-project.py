from collections import deque

class Solution:
    def minTime(self, duration, dependencies):
        n = len(duration)
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in dependencies:
            adj[u].append(v)
            indegree[v] += 1

        queue = deque()
        time_to_complete = [0] * n

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                time_to_complete[i] = duration[i]

        visited_count = 0
        while queue:
            u = queue.popleft()
            visited_count += 1

            for v in adj[u]:
                time_to_complete[v] = max(time_to_complete[v], time_to_complete[u] + duration[v])
                indegree[v] -= 1

                if indegree[v] == 0:
                    queue.append(v)
        if visited_count != n:
            return -1
        return max(time_to_complete)