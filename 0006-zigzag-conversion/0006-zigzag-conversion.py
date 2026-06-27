class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case: If there's only 1 row or not enough characters to zigzag
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize an array of strings for each row
        rows = [""] * numRows
        curr_row = 0
        going_down = False
        
        # Step through each character in the string
        for char in s:
            rows[curr_row] += char
            
            # Change direction when we hit the top or bottom row
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
                
            # Move up or down depending on the direction
            curr_row += 1 if going_down else -1
            
        # Combine all rows into a single string
        return "".join(rows)