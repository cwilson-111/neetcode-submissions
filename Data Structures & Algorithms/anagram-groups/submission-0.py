class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #mapping charCount to list of anagrams 

        for s in strs:
            count = [0] * 26 #from a to z

            for c in s:
                count[ord(c) - ord("a")] += 1#subtract index at c from askey value a, a - a = 0, z - a = 25

            result[tuple(count)].append(s) #make a non mutable list aka a tuple

        return list(result.values())
        #O(m * n)