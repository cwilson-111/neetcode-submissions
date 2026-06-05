class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        #iterate thru range of the length of the list size - size of the window + 1
        for i in range(len(nums) - k + 1):
            #max i initial is value at first i
            maxi = nums[i]
            for j in range(i, i + k):
                #slide window, range from i value to i + window length (e.g. 3)
                #max i is now the max between previous max i and the value at index j in nums
                maxi = max(maxi, nums[j])
            #add this new value to the output arr
            output.append(maxi)

        return output