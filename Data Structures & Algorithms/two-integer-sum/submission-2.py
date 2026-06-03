class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}  
        
        #enumerate retrieves index and value 
        #get initial number needed to finish target 
        for i, num in enumerate(nums):
            complement = target - num

            #returns the compliment index
            if complement in hmap:
                return [hmap[complement], i]
            
            hmap[num] = i
            
        return []