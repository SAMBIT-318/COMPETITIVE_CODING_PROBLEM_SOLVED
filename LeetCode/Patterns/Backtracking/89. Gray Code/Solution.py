class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 1 << n is equivalent to 2^n
        return [i ^ (i >> 1) for i in range(1 << n)]