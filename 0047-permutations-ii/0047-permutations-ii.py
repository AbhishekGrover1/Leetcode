class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        # Sort to place duplicates adjacent to each other
        nums.sort()
        used = [False] * len(nums)
        
        def backtrack(current_permutation):
            # Base Case: Found a complete permutation
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation))
                return
            
            for i in range(len(nums)):
                # Skip if this specific element index is already in use
                if used[i]:
                    continue
                
                # Skip duplicates: if the previous identical element hasn't been used yet
                # in this path, processing the current one creates a duplicate sequence.
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # Make choice
                used[i] = True
                current_permutation.append(nums[i])
                
                # Recursive exploration
                backtrack(current_permutation)
                
                # Undo choice (Backtrack)
                current_permutation.pop()
                used[i] = False
                
        backtrack([])
        return result