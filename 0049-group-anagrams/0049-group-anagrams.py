from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # A dictionary where each value defaults to an empty list
        anagram_map = defaultdict(list)
        
        for string in strs:
            # Sorting the string characters creates a uniform key for all anagrams
            # Tuples are immutable and can be used as dictionary keys
            sorted_key = tuple(sorted(string))
            
            # Group the original string under its corresponding key
            anagram_map[sorted_key].append(string)
            
        # Return the collected groups of anagrams
        return list(anagram_map.values())