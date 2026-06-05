class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #loop thru each row and column
        for i in matrix:
            for j in i:
                #if j = target value return true
                if j == target:
                    return True 
        return False