class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        # Continue searching left for the first position
                        right = mid - 1
                    else:
                        # Continue searching right for the last position
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        # Find both boundaries
        start = findBound(isFirst=True)
        end = findBound(isFirst=False)
        
        return [start, end]