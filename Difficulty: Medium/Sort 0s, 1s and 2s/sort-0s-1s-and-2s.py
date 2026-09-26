class Solution:
    def sort012(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                # Swap mid and low, increment both
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # 1 is in the correct place, just move mid
                mid += 1
            else:
                # Swap mid and high, decrement high
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr