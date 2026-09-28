class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # We always want to run binary search on the smaller array for efficiency.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            # Partition both arrays
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # Find the boundary values (handling edge cases with infinity)
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Check if we found the perfect partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If total length is even, median is average of the two middle elements
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                # If total length is odd, median is the max of the left side
                else:
                    return float(max(maxLeftX, maxLeftY))
            
            # If we are too far right in nums1, move left
            elif maxLeftX > minRightY:
                high = partitionX - 1
                
            # If we are too far left in nums1, move right
            else:
                low = partitionX + 1