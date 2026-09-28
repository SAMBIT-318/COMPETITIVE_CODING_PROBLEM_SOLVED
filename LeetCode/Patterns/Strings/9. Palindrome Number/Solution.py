class Solution(object):
    def isPalindrome(self, x):
        """:type x: int
        :rtype: bool
        """
        # Negative numbers and numbers ending in 0 (other than 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
            
        # When the length is an odd number, we can get rid of the middle digit by reversed_half // 10
        # For example, when x = 12321, at the end of the loop x = 12, reversed_half = 123
        return x == reversed_half or x == reversed_half // 10