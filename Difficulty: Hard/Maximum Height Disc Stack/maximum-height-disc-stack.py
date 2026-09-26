class Solution:
    def maxStackHeight(self, r, h):
        n = len(r)
        if n == 0:
            return 0
        discs = [(r[i], h[i]) for i in range(n)]
        discs.sort(key=lambda x: (x[0], -x[1]))

        max_h = max(h)
        bit = [0] * (max_h + 1)
        def query(idx):
            res = 0
            while idx > 0:
                if bit[idx] > res:
                    res = bit[idx]
                idx -= idx & (-idx)
            return res
        def update(idx, val):
            while idx <= max_h:
                if val > bit[idx]:
                    bit[idx] = val
                idx += idx & (-idx)

        ans = 0
        for radius, height in discs:
            max_prev = query(height - 1)
            current_stack = max_prev + height
            if current_stack > ans:
                ans = current_stack
            update(height, current_stack)

        return ans