class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nlist = []
        for i in nums:
            if i not in nlist:
                nlist.append(i)
            else:
                return True
        return False