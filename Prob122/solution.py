class Solution:

    def maxProfit(self, prices) -> int:
        maxProfit = 0

        curMin = prices[0]
        curMax = prices[0]

        lookingForMin = True
        for x in range(len(prices)):
            price = prices[x]
            if lookingForMin:
                if curMin > price:
                    curMin = price
                else:
                    curMax = price
                    lookingForMin = not lookingForMin
            if not lookingForMin:
                if curMax < price:
                    curMax = price
                else:
                    # "Selling" a stock
                    lookingForMin = not lookingForMin
                    maxProfit += curMax - curMin
                    curMax = price
                    curMin = price

        return maxProfit
    
# 5, 3, 2, 1, 0, -1, -2, -3
def Testing():
    sol = Solution()
    print(sol.maxProfit([3, 5, 7, 9, 11, 3, 4, 5]))
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([1,2,3,4,5]))
    print(sol.maxProfit([7,6,4,3,1]))
    print(sol.maxProfit([1]))

Testing()