class Solution:
    def palindromicStrings(self, n: int, k: int) -> int:
        #code here
        MOD = 10**9 + 7
        total_count = 0

        perm = [1] * (k + 1)
        for i in range(1, k + 1):
            perm[i] = (perm[i - 1] * (k - i + 1)) % MOD

        for L in range(1, n + 1):
            m = L // 2
            if L % 2 == 0:
                if m <= k:
                    total_count = (total_count + perm[m]) % MOD
            else:
                if m + 1 <= k:
                    total_count = (total_count + perm[m + 1]) % MOD

        return total_count