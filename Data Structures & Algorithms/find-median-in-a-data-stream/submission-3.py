class MedianFinder:

    def __init__(self):
        #init empty array
        self.arr = []

    def addNum(self, num: int) -> None:
        #adding num to arr
        self.arr.append(num)

    def findMedian(self) -> float:
        #start by sorting to find acc median
        #then get len and mid
        self.arr.sort()
        n = len(self.arr)
        mid = n // 2

        #check to see if median is even, if it is return sum of two mid numbers
        if n % 2 == 0:
            return (self.arr[mid - 1] + self.arr[mid]) / 2.0
            
        # if odd return mid number
        return float(self.arr[mid])
            
        