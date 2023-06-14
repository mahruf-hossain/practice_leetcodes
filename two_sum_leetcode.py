"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
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
* 2 <= nums.length <= 104
* -109 <= nums[i] <= 109
* -109 <= target <= 109
Only one valid answer exists."""



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} # create a dictionary called "seen"
        diff = target - num # create a variable called diff 
        for i, num in enumerate(nums): # looping through the indices and elements of the list
            if diff in seen: # checking a conditional if diff is in the dictionary 1. if diff is not in the dict seen, add that diff to that dict seen , 2. if diff is in dict continue as it is
                return [seen[diff], i] # return a list as expected
            seen[num] = i
        return []
        
    
