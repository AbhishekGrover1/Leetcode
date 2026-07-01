class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :type rtype: List[List[int]]
        """
        result = []
        # 1. Sort the candidates to handle duplicates easily
        candidates.sort()
        
        def backtrack(start_idx, current_combo, current_sum):
            # Base Case: Found a valid combination
            if current_sum == target:
                result.append(list(current_combo))
                return
            
            # Base Case: Exceeded target limit
            if current_sum > target:
                return
            
            # Explore choices starting from start_idx
            for idx in range(start_idx, len(candidates)):
                # 2. Skip duplicate numbers at the same recursion depth
                if idx > start_idx and candidates[idx] == candidates[idx - 1]:
                    continue
                
                # Small optimization: If the current number exceeds remaining target, 
                # all subsequent numbers will too (since the array is sorted).
                if current_sum + candidates[idx] > target:
                    break
                    
                # Include the candidate
                current_combo.append(candidates[idx])
                
                # 3. Move to idx + 1 because each element can only be used once
                backtrack(idx + 1, current_combo, current_sum + candidates[idx])
                
                # Backtrack: Remove the candidate
                current_combo.pop()
                
        backtrack(0, [], 0)
        return result