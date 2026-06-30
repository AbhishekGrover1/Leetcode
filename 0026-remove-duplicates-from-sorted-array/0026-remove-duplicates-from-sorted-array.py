class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Pointer to place the next unique element
        k = 1 
        
        # Scan through the array starting from the second element
        for i in range(1, len(nums)):
            # If current element is different from the last unique element found
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
                
        return k