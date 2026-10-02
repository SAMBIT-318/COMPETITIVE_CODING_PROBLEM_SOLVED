class Solution(object):
    def generateParenthesis(self, n):
        """:type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(current_path, open_count, close_count):
            if len(current_path) == 2 * n:
                result.append("".join(current_path))
                return
                
            if open_count < n:
                current_path.append('(')
                backtrack(current_path, open_count + 1, close_count)
                current_path.pop()
                
            if close_count < open_count:
                current_path.append(')')
                backtrack(current_path, open_count, close_count + 1)
                current_path.pop()
                
        backtrack([], 0, 0)
        return result