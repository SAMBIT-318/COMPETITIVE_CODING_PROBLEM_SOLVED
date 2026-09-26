class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        dp = [float('inf')] * (x + 1)
        dp[0] = 0
        for i in range(1, x + 1):
            cost_small = dp[max(0, i - s)] + cs
            cost_medium = dp[max(0, i - m)] + cm
            cost_large = dp[max(0, i - l)] + cl
            dp[i] = min(cost_small, cost_medium, cost_large)

        return dp[x]