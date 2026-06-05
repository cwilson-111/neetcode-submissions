class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        #loop thru nums
        for num in nums:
            #use bitwise XOR to add everything to result
            #if two numbers are ^ together they = 0, so 1,1,2,2,3 = 3
            result ^= num
        return result
