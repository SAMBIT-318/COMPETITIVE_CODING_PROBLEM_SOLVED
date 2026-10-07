class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        rem_l = 0
        rem_r = 0
        for char in s:
            if char == '(':
                rem_l += 1
            elif char == ')':
                if rem_l > 0:
                    rem_l -= 1
                else:
                    rem_r += 1
                    
        res = []
        
        def dfs(index, left_count, rem_l, rem_r, path):
            if index == len(s):
                if rem_l == 0 and rem_r == 0 and left_count == 0:
                    res.append("".join(path))
                return
            
            char = s[index]
            
            if char == '(' and rem_l > 0:
                if index == 0 or s[index] != s[index - 1] or len(path) == 0 or path[-1] != char:
                    dfs(index + 1, left_count, rem_l - 1, rem_r, path)
            elif char == ')' and rem_r > 0:
                if index == 0 or s[index] != s[index - 1] or len(path) == 0 or path[-1] != char:
                    dfs(index + 1, left_count, rem_l, rem_r - 1, path)
            
            path.append(char)
            if char != '(' and char != ')':
                dfs(index + 1, left_count, rem_l, rem_r, path)
            elif char == '(':
                dfs(index + 1, left_count + 1, rem_l, rem_r, path)
            elif char == ')' and left_count > 0:
                dfs(index + 1, left_count - 1, rem_l, rem_r, path)
            path.pop()

        dfs(0, 0, rem_l, rem_r, [])
        return res if res else [""]