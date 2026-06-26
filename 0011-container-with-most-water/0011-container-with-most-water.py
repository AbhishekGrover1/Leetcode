class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate the width between the two vertical lines
            width = right - left
            
            # The height of the water is constrained by the shorter line
            current_height = min(height[left], height[right])
            
            # Calculate the area and update max_water if the current one is larger
            current_water = width * current_height
            max_water = max(max_water, current_water)
            
            # Move the pointer that points to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
        
        