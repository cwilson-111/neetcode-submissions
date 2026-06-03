class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap={}
        for num in nums:
            hmap[num] = hmap.get(num,0) + 1

            if hmap.get(num) > 1:
                return True
        return False