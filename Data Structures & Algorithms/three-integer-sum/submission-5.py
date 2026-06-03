class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            #sum of the three numbers is equal to 
            #sum of other three numbers
            #arrange in any order to achieve this
            if a> 0:
                break
            
            if i > 0 and a== nums[i - 1]:
                continue
            # use two pointers for left and right side
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a+ nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1  #sum too big, make it smaller by moving right 
                elif three_sum < 0:
                    l += 1  #sum too small, make it bigger by moving left
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                   #skip dupe values from the left side
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1             
        return res

