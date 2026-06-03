class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}  # Stores value -> index pairs
        
        # enumerate gives you both the index (i) and the actual number (num)
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the needed number is already in our hash map
            if complement in hmap:
                # Return the index of the complement and the current index
                return [hmap[complement], i]
            
            # If not found, add the current number and its index to the map
            hmap[num] = i
            
        return []