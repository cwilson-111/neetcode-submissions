class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest = 0

        for num in num_set:
            # only start if it's the beginning of a sequence
            #if num -1 does not exist, set current = num, length = 1 and start
            if num - 1 not in num_set:
                current = num
                length = 1
                #while current value + 1 is in set, increment current and length values
                while current + 1 in num_set:
                    current += 1
                    length += 1
                #set longest to the max length
                longest = max(longest, length)

        return longest


