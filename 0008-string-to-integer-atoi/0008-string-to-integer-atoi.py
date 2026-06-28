class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define 32-bit signed integer boundaries
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        
        # Step 1: Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # Step 2: Check for signedness
        sign = 1
        index = 0
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
            
        # Step 3 & 4: Convert digits and handle potential overflow
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            # Check overflow before multiplying
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
                
            result = result * 10 + digit
            index += 1
            
        return sign * result