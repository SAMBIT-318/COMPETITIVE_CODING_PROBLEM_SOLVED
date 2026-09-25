class Solution(object):
    def threeSumClosest(self, nums, target):
        # 1. Sort the array to enable two pointers
        nums.sort()
        closest_sum = float('inf')
        
        # 2. Iterate and fix one number at a time
        for i in range(len(nums) - 2):
            # Minor optimization: skip identical fixed numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            # 3. Two Pointers for the remaining two numbers
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we hit the target exactly, we are done
                if current_sum == target:
                    return current_sum
                    
                # Update closest_sum if we found a strictly closer match
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                # Adjust pointers to get closer to the target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum