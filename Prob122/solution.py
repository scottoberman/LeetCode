class Solution:

    def maxProfit(self, prices) -> int:
        maxProfit = 0

        daysAndPrices = enumerate(prices)

        daysAndPricesSorted =  sorted(daysAndPrices, key=lambda x: x[1], reverse=True) # change x[1] to x[0]

        x = 0
        maxFound = False

        # Using whiles is more hideous than breaking fors
        # but just doing so for ez single return.
        while not maxFound and x < len(daysAndPricesSorted):
            y = len(daysAndPricesSorted) - 1
            while not maxFound and y > x:
                potentialProfit = daysAndPricesSorted[x][1] -  daysAndPricesSorted[y][1]
                dayBuy = daysAndPricesSorted[x][0]
                daySell = daysAndPricesSorted[y][0]
                if potentialProfit > maxProfit and \
                    dayBuy < daySell:
                    maxProfit = potentialProfit
                    maxFound = True
                else:
                    y -= 1

            if not maxFound:
                x += 1
        
        return maxProfit
    

def Testing():
    sol = Solution()
    print(sol.maxProfit([3, 5, 7, 9, 11, 3, 4, 5]))

Testing()