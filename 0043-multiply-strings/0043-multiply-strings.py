class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :type rtype: str
        """
        # Edge case: if either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
            
        # Initialize an array to store the intermediate addition results
        result = [0] * (len(num1) + len(num2))
        
        # Loop through both strings backward
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Multiply the two single digits
                mul = int(num1[i]) * int(num2[j])
                
                # Find the target indices in the result array
                p1 = i + j
                p2 = i + j + 1
                
                # Add current multiplication product to the existing value at p2
                total = mul + result[p2]
                
                # Update positions with the new digit value and the carryover
                result[p2] = total % 10
                result[p1] += total // 10
                
        # Skip leading zeros if the first position didn't receive a carry
        start_idx = 0
        while start_idx < len(result) and result[start_idx] == 0:
            start_idx += 1
            
        # Convert the integer array chunks into a final string sequence
        return "".join(map(str, result[start_idx:]))