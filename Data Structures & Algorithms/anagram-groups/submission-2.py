class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # list of dictionarys for counts of each word
        sorted_words = {}

        for word in strs:
            sorted_word = "".join(sorted(word)) 
            if sorted_word in sorted_words:
                sorted_words[sorted_word].append(word)
            else:
                sorted_words[sorted_word] = [word]

        return list(sorted_words.values())
                
        