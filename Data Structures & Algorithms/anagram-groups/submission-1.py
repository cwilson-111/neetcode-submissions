class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        MAX_CHAR = 26
        hmap = {}


        for word in strs:
            freq = [0] * MAX_CHAR

            for char in word:
                freq[ord(char) - ord('a')] += 1

            key = tuple(freq)

            if key not in hmap:
                hmap[key] = []
            hmap[key].append(word)
        return list(hmap.values())

        
