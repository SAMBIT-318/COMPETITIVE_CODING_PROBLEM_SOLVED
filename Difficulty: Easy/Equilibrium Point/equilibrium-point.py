class Solution:
    def findEquilibrium(self, arr):
        #Code Here
        total_sum = sum(arr)
        left_sum = 0

        for i, val in enumerate(arr):
            right_sum = total_sum - left_sum - val

            if left_sum == right_sum:
                return i

            left_sum += val

        return -1