# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical linesare drawn such that the two endpoints
# of the line i is at (i, ai) and (i, 0). Find two lines, which, together
# with the x-axis forms a container, such that the container contains the most
# water.

# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height) -> int:

        leftX = 0
        rightX = len(height) - 1

        aMax = 0

        while leftX != rightX:
            leftY = height[leftX]

            rightY = height[rightX]

            area = (rightX - leftX) * min(rightY, leftY)

            if rightY > leftY:
                leftX += 1
            else:
                rightX -= 1

            aMax = max(area, aMax)

        return aMax



def Test():
    sol = Solution()
    print(sol.maxArea([13,14,15,16,17]))
    print(sol.maxArea([1, 1]))
    print(sol.maxArea([4,3,2,1,4]))
    print(sol.maxArea([1,2,1]))
        


Test()
        
        