class Solution:
    def maxSweetness(self, sweetness: list[int], k: int) -> int:
        def can_divide(target):
            pieces = 0
            current_sweetness = 0

            for s in sweetness:
                current_sweetness += s
                if current_sweetness >= target:
                    pieces += 1
                    current_sweetness = 0

            return pieces >= k + 1
        low = min(sweetness)
        high = sum(sweetness)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if can_divide(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
