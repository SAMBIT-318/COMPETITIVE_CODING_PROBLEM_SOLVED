class Solution:
    def pairCount(self, x, y):
        #code here
        if y % x != 0:
            return 0

        k = y // x
        distinct_prime_factors = 0

        d = 2
        while d * d <= k:
            if k % d == 0:
                distinct_prime_factors += 1
                while k % d == 0:
                    k //= d
            d += 1

        if k > 1:
            distinct_prime_factors += 1

        return 1 << distinct_prime_factors