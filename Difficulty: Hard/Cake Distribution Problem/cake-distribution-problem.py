class Solution:
    def maxSweetness(self, sweetness: list[int], k: int) -> int:

        # Helper function to check if we can get at least k+1 pieces 
        # where each piece has a sweetness >= target
        def can_divide(target):
            pieces = 0
            current_sweetness = 0

            for s in sweetness:
                current_sweetness += s
                if current_sweetness >= target:
                    pieces += 1
                    current_sweetness = 0

            return pieces >= k + 1

        # Search space boundaries
        low = min(sweetness)
        high = sum(sweetness)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if can_divide(mid):
                # If we can divide, mid is a potential answer, try for a higher one
                ans = mid
                low = mid + 1
            else:
                # If we can't, target is too high, try a lower one
                high = mid - 1

        return ans