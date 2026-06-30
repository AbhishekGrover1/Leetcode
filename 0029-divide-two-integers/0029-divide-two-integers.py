class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Constants for 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the quotient
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with absolute values
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        quotient = 0

        # Loop until the dividend is less than the divisor
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1
            
            # Left shift the divisor to find the highest power of 2 multiple
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract the largest found multiple from dividend
            abs_dividend -= temp_divisor
            # Add the multiple to the quotient
            quotient += multiple

        # Apply the sign
        if negative:
            quotient = -quotient

        # Clamp the result within 32-bit signed integer limits
        return max(INT_MIN, min(INT_MAX, quotient))