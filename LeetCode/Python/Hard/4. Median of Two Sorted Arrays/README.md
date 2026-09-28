# 📝 4. Median of Two Sorted Arrays (LeetCode)

🔗 [Problem Link](https://leetcode.com/problems/median-of-two-sorted-arrays/)

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red) ![Language](https://img.shields.io/badge/Language-Python-blue)

### 💡 Tags
Array, Binary Search, Divide and Conquer

### 🚀 Performance
- **Runtime:** 4 ms
- **Memory:** 12.7 MB

---

### 📜 Problem Description

Given two sorted arrays  `nums1`  and  `nums2`  of size  `m`  and  `n`  respectively, return  **the median**  of the two sorted arrays.

The overall run time complexity should be  `O(log (m+n))` .

**Example 1:**

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

```

**Example 2:**

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

```

**Constraints:**

	
- `nums1.length == m`
	
- `nums2.length == n`
	
- `0 <= m <= 1000`
	
- `0 <= n <= 1000`
	
- `1 <= m + n <= 2000`
	
- `-106 <= nums1[i], nums2[i] <= 106`