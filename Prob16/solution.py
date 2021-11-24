from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        numsSort = sorted(nums)
    
        sum = numsSort[0] + numsSort[1] + numsSort[2]
        diff = abs(sum - target)
        
        # Cursors moving from left to right.
        for x in range (len(numsSort)):
            for y in range (x + 1, len(numsSort)):
                for z in range (y + 1, len(numsSort)):
                    sumNew = numsSort[x] + numsSort[y] + numsSort[z]
                    if abs(sumNew - target)  < diff:
                        sum = sumNew
                        diff = abs(sum - target)
                        
                        if sum == target:
                            return sum
                        
                    if numsSort[x] + numsSort[y] + numsSort[z] > target:
                        break
                    
        return sum
    
                    
    
    
def Test():
    sol = Solution()
    
    print(sol.threeSumClosest([5,4,3,2,1], 15)) # 12
    print(sol.threeSumClosest([15, 12, 6, 1], 4)) # 19
    print(sol.threeSumClosest([12, 5, 3], 6)) # 20
    
    
Test()