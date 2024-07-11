"""
Author : strivingengineer

Problem: https://leetcode.com/problems/contains-duplicate/description/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# Approach 1: We can use brute force approach of using two nested loop which results in
# Time complexity of O(n^2)
# Space complexity of O(1)
# where n is the length of the array.


class Solution:
    def containsDuplicate(self, nums) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# Approach 2: We can use sorting to sort the input list so that if any duplicate exists in the list will be adjacent so that we just have to compare the next value using two pointers
# Time complexity of O(n(logn))
# Space complexity of O(1)
# where n is the length of the array.


class Solution:
    def containsDuplicate1(self, nums) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


# Approach 3: We can use the set of python to store the seen number and the check if the number already exists in set or not
# Time complexity of O(n)
# Space complexity of O(n)
# where n is the length of the array.


class Solution:
    def containsDuplicate2(self, nums) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False


# Approach 4: We can use the dictionary of python to store the seen number and the check if the number already exists in hashmap or not
# Time complexity of O(n)
# Space complexity of O(n)
# where n is the length of the array.


class Solution:
    def containsDuplicate3(self, nums) -> bool:
        seen = dict()

        for i in nums:
            if i in seen and seen[i] >= 1:
                return True
            seen[i] = seen.get(i, 0) + 1
        return False


# Approach 5: We can use the set of python to compare the length of input list and length of set of input list if both are same then no duplicate else it contains duplicate
# Time complexity of O(n)
# Space complexity of O(n)
# where n is the length of the array.


class Solution:
    def containsDuplicate4(self, nums) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True

        # return len(set(nums)) != len(nums)  as one liner
