class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Pointer to place the next valid element 
        k = 0

        # Scan through the array 
        for i in range(len(nums)):
            # If the current element is the not the value we want to remove
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k 