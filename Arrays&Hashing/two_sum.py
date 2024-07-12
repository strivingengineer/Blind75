"""
Author : strivingengineer


Problem: https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

"""
Approach 1: We can use a nested loop to iterate over the array and check if sum of value of two indexs in nums is
equal to target then return those indexs

Time complexity of O(n^2)
Space complexity of  O(n) , where n is the length of the array

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


"""
Approach 2: We can use dictionary to store the pair of value to index of list and then check if the value which is required to
compliment (target-current_value) already present in dictionary , if yes return current index and index of compliment from 
dictionary

Time complexity of O(n)
Space complexity of  O(n)  where n is the length of the array

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            expected_value = target - nums[i]

            if expected_value in seen:
                return [seen[expected_value], i]

            seen[nums[i]] = i
