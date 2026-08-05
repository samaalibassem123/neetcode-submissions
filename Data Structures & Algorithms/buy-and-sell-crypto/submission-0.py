class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        Mprofit = 0
        while r < len(prices):
            print(prices[l] , prices[r])
            if prices[l] < prices[r] :
                Mprofit = max(Mprofit, (prices[r] - prices[l]))
                r = r + 1
            else:
                l = r
                r = l + 1
        return Mprofit