class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,j in enumerate(nums): 
            complement = target - j 

            if complement in hmap:
                return [hmap[complement],i]
            hmap[j] = i