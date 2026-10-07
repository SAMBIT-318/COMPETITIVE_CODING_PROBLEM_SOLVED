'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    def maxPathSum(self, root):
        max_sum = float('-inf')
        
        def helper(node):
            nonlocal max_sum
            if not node:
                return float('-inf')
            
            # Leaf node
            if not node.left and not node.right:
                return node.data
            
            left_sum = helper(node.left)
            right_sum = helper(node.right)
            if node.left and node.right:
                max_sum = max(max_sum, left_sum + right_sum + node.data)
                return max(left_sum, right_sum) + node.data
            
            return (left_sum if node.left else right_sum) + node.data

        val = helper(root)
        
        if max_sum == float('-inf'):
            return -1
            
        return max_sum