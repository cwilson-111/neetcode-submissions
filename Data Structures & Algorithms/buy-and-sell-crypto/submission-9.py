class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #init vaiables
        buy = float('inf')
        max_profit = 0

        #loop thru all prices, if i less than current buy value, buy = i
        for i in prices:
            if i < buy:
                buy = i
            #when i !< buy find profit
            else:
                profit = i - buy
                
                #find max profit
                if profit > max_profit:
                    max_profit = profit

        return max_profit