class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))

            if sorted_word not in hash:
                hash[sorted_word] = []
                hash[sorted_word].append(strs[i])
            else:
                hash[sorted_word].append(strs[i])

        return list(hash.values())