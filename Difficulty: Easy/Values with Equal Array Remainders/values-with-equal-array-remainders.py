import math

class Solution:
    def sameMod(self, arr):
        #code here
        g = 0
        for x in arr:
            g = math.gcd(g, abs(x - arr[0]))

        if g == 0:
            return -1

        divisors_count = 0
        limit = int(math.isqrt(g))
        for d in range(1, limit + 1):
            if g % d == 0:
                divisors_count += 1
                if d * d != g:
                    divisors_count += 1

        return divisors_count