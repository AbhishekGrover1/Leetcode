class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Base case: if the input string is empty, return an empty list
        if not digits:
            return []
            
        # Map digits to their corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, current_combination):
            # If the current combination length matches the input digits length,
            # we've successfully formed a complete combination
            if len(current_combination) == len(digits):
                res.append("".join(current_combination))
                return
                
            # Get the letters that the current digit maps to
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # Loop through the letters and recurse
            for letter in letters:
                current_combination.append(letter)  # Choose
                backtrack(index + 1, current_combination)  # Explore
                current_combination.pop()  # Backtrack (Undo choice)
                
        # Start the backtracking process from index 0 with an empty combination list
        backtrack(0, [])
        return res