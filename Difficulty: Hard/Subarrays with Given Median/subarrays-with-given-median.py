class Solution:
    def countSubarray(self, arr: list[int], m: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        def count_at_least(val: int) -> int:
            freq = [0] * (2 * n + 1)

            cur_sum = 0
            freq[n] = 1
            total_valid = 0
            ans = 0

            for x in arr:
                if x >= val:
                    total_valid += freq[cur_sum + n]
                    cur_sum += 1
                else:
                    cur_sum -= 1
                    total_valid -= freq[cur_sum + n]

                ans += total_valid
                freq[cur_sum + n] += 1

            return ans

        result = (count_at_least(m) - count_at_least(m + 1)) % MOD
        return result