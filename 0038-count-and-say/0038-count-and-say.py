class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Base case
        current_str = "1"
        
        # Perform the transition n-1 times
        for _ in range(n - 1):
            next_str_chunks = []
            i = 0
            
            while i < len(current_str):
                count = 1
                # Count identical consecutive characters
                while i + 1 < len(current_str) and current_str[i] == current_str[i + 1]:
                    count += 1
                    i += 1
                
                # Append the count and the digit itself
                next_str_chunks.append(str(count))
                next_str_chunks.append(current_str[i])
                i += 1
                
            # Build the next sequence string
            current_str = "".join(next_str_chunks)
            
        return current_str