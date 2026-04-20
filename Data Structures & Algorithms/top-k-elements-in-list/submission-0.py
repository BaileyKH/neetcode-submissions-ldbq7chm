class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        occurence = [[] for _ in range(len(nums) + 1)]
        k_elements = []

        for i,num in enumerate(nums):
            hash[num] = hash.get(num, 0) + 1

        for key,value in hash.items():
            occurence[value].append(key)

        for item in reversed(occurence):
            if len(k_elements) != k and item != []:
                k_elements.extend(item)

        return k_elements

        