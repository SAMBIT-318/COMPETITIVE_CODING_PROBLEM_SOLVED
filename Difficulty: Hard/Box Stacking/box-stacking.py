class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        n = len(height)
        boxes = []
        for i in range(n):
            h, w, l = height[i], width[i], length[i]
            boxes.append((min(w, l), max(w, l), h))
            boxes.append((min(h, l), max(h, l), w))
            boxes.append((min(h, w), max(h, w), l))
        boxes.sort(key=lambda b: (b[0] * b[1], b[1], b[0]), reverse=True)

        m = len(boxes)
        dp = [b[2] for b in boxes]
        for i in range(1, m):
            w_i, l_i, h_i = boxes[i]
            for j in range(i):
                w_j, l_j, _ = boxes[j]
                if w_i < w_j and l_i < l_j:
                    dp[i] = max(dp[i], dp[j] + h_i)

        return max(dp)