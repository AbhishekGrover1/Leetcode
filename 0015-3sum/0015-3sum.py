class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()  # Sort the array first
        
        for i in range(len(nums) - 2):
            # If the current number is greater than 0, the remaining numbers 
            # will also be greater than 0, so no triplet can sum to 0.
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Two-pointer approach
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Sum is too small, move left pointer right
                elif total > 0:
                    right -= 1  # Sum is too large, move right pointer left
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Move both pointers past the last unique elements checked
                    left += 1
                    right -= 1
                    
        return res