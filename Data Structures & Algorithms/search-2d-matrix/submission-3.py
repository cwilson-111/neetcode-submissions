class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # #loop thru each row and column
        # for row in matrix:
        #     for col in row:
        #         #if col = target value return true
        #         if col == target:
        #             return True 
        # return False


        #binary search for O(m * log n)
        #iterate through each row with left = 0, and right starting at the end
        for row in matrix:
            left,right = 0, len(row) - 1

            #while left <= right we will check values to see if the target is in the middle
            while left <= right:
                #finding middle of the row
                mid = (left + right) // 2
                
                #if target is in the middle, return true
                if row[mid] == target:
                    return True
                #move left pointer to the right by 1 if less than target
                elif row[mid] < target:
                    left = mid + 1
                else:
                    #Move right pointer to the left by 1 if greater than target
                    right = mid - 1
        return False
