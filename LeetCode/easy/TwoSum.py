"""
Date : Jul 3rd, 2025

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

# My Solution

class Solution : 
    def twoSum(self, nums: list[int], target: int) -> list[int] : 
        for i in range(0, len(nums) - 1) :
            if nums[i] < target :
                    a = target - nums[i]
                    for j in range(i + 1, len(nums)) :
                         if nums[j] == a :
                              return [i, j]
                         else : continue
            else : continue
        
        return 0
    
# One-pass Hash Table

class Solution2 :
    def twoSum(self, nums: list[int], target: int) -> list[int] : 
        hashmap = {}
        for i in range(len(nums)) :
            complement = target - nums[i]
            if complement in hashmap :
                return [i, complement]
            hashmap[nums[i]] = i
        return []

nums = [3, 3]
target = 6

sol = Solution()
print(sol.twoSum(nums, target))