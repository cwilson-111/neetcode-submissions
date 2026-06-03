class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #set initial hashmap to empty

        for num in nums:
            count[num] = 1 + count.get(num,0) #adding elements to hasmap based on frequency

        arr = [] #make an empty array for sorting
        for num, cnt in count.items():
            arr.append([cnt, num]) #add items in count to the array 
        arr.sort() # sort the array

        res = [] #make a new array for the result

        while len(res) < k: 
            res.append(arr.pop()[1]) #append the first element in the list to the new array based off size k
        return res

