class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string in a different list
        # loop through list using range() or enumerate()
        # have a dictionary(key=sorted_word, value=list(word index))
        # all anagarams will have the same sorted key and then at the end just make a list from the indices

        sorted_words = ["".join(sorted(x)) for x in strs]

        diction = {}
        for i, word in enumerate(sorted_words):
            if word in diction:
                diction[word].append(strs[i])
            else:
                diction[word] = [strs[i]]

        result = list(diction.values())




        return result
        