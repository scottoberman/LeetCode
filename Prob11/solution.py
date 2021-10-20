# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical linesare drawn such that the two endpoints
# of the line i is at (i, ai) and (i, 0). Find two lines, which, together
# with the x-axis forms a container, such that the container contains the most
# water.

# Notice that you may not slant the container.

from dataclasses import dataclass

@dataclass
class HeightInfo:
    height: int
    pos: int

class Solution:
    def maxArea(self, height) -> int:

        aMax = 0

        for index1 in range(len(height) - 1):
            for index2 in range(index1, len(height)):
                leftX = index1
                leftY = height[index1]

                rightX = index2
                rightY = height[index2]

                area =  (rightX - leftX) * (min(rightY, leftY))

                aMax = max(aMax, area)

        return aMax



def Test():
    sol = Solution()
    print(sol.maxArea([13,14,15,16,17]))
    print(sol.maxArea([1, 1]))
    print(sol.maxArea([4,3,2,1,4]))
    print(sol.maxArea([1,2,1]))
        


Test()
        
        