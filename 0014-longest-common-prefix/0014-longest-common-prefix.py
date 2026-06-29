class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Iterate through the character of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]

            # compare this character with the character at the same index in all other strings 
            for string in strs[1:]:
                # if the current string is shorter than 'i' or characters don't match 
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]

        return strs[0]
        