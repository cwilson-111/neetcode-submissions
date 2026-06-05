class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #decide that we are comparing expected numbers to actual numbers
        res = len(nums) 
    
        #iterate thru the list
        for i,num in enumerate(nums):
            #take the XOR of the Index and the number,
            #res = res ^ i ^ num where res starts as the length of nums, i is the current Index
            #and num is the current number value at that index 
            res ^= i ^ num
        return res
