from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        word_count = Counter(words)
        result = []
        
        # Run sliding window for each possible character offset
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            words_used = 0
            
            # Slide the window across the string
            while right + word_len <= s_len:
                # Get the next word from the right
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    words_used += 1
                    
                    # If a word is overused, shrink the window from the left
                    while current_count[word] > word_count[word]:
                        removed_word = s[left:left + word_len]
                        current_count[removed_word] -= 1
                        words_used -= 1
                        left += word_len
                        
                    # If all words match perfectly, add the start index
                    if words_used == num_words:
                        result.append(left)
                else:
                    # Reset the window if a completely invalid word is hit
                    current_count.clear()
                    words_used = 0
                    left = right
                    
        return result