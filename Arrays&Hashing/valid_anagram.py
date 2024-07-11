"""
Author : strivingengineer

Problem: https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""

# Approach 1: We can use inbuilt sorted function and check if both input string results into same after sorting
# Time complexity of O(n(logn))
# Space complexity of O(1)
# where n is the length of the array.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


"""
Approach 2: We can use dictionary to store values of first input word and its occurance and the iterate over second word to check if
its is having its character in dictionary if not immediately return False else reduce current occurance of char by 1 and in the end 
iterate over the dictionary values to check if it is less than 1 if yes return False else in the end return True
"""
# Time complexity of O(n)
# Space complexity of O(n)
# where n is the length of the array.


class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        values = {}

        for item in s:
            values[item] = values.get(item, 0) + 1

        for item in t:
            if item not in values:
                return False
            values[item] -= 1

        for value in values.values():
            if value != 0:
                return False
        return True


"""
Approach 2: It is slightly optimized in term of reducing the extra iteration on dictionary and doing that check in second loop
"""
# Time complexity of O(n)
# Space complexity of O(n)
# where n is the length of the array.


class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        values = {}

        for item in s:
            values[item] = values.get(item, 0) + 1

        for item in t:
            if item not in values or values[item] <= 0:
                return False
            values[item] -= 1

        return True


"""
Approach 3: In this we are using inbuild Counter which create dictionary of values and then doing comparision on both Counters
"""
# Time complexity of O(n)
# Space complexity of O(n)
# where n is the length of the array.

from collections import Counter


class Solution:
    def isAnagram3(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)


"""
Approach 4: First of all create array with length of 26, then iterate through s string. Every time we 
calculate subtraction with ASCII values, why "a" because "a" is the smallest ASCII value and 
the ASCII values of all lowercase letters are sequential. If we subtract ASCII value of "a" 
from ASCII value of current character, you should be able to retrieve the order of those alphabets
"""
# Time complexity of O(n)
# Space complexity of O(26) ~ O(1)
# where n is the length of the array.


class Solution:
    def isAnagram4(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = [0] * 26

        for char in s:
            count[ord(char) - ord("a")] += 1

        for char in t:
            if count[ord(char) - ord("a")] == 0:
                return False
            count[ord(char) - ord("a")] -= 1

        return True
