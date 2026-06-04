class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #going to search from each side so two pointers at each end of array
        left = 0
        right = len(nums) - 1

        #loop until pointer cross
        while left <= right:
            #find exact middle
            mid = (left + right) // 2

            #condition to see if target was at mid
            if target == nums[mid]:
                return mid
            #if target is less than mid, move pointer left
            elif target < nums[mid]:
                right = mid - 1
            #if target > mid, move pointer right
            else:
                left = mid + 1
        return -1
        