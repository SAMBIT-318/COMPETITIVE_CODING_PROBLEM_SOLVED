class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        insertions = 0
        open_needed = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                open_needed += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    insertions += 1
                    i += 1
                
                if open_needed > 0:
                    open_needed -= 1
                else:
                    insertions += 1

        return insertions + open_needed * 2