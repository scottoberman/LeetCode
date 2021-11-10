# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:

# Input: nums = [1]
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leftIndex  = 0
        rightIndex = len(nums) - 1
        leftIndex = rightIndex - 1
        nextPerm = False

        if leftIndex < 0:
            return

        while not nextPerm:
            if nums[leftIndex] < nums[rightIndex]:
                nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
                nextPerm = True
            elif leftIndex > 0:
                leftIndex -= 1
            else:
                rightIndex -= 1
                leftIndex = rightIndex - 1

            if leftIndex == -1:
                nextPerm = True

        if leftIndex == -1:
            # Reverse all numbers or whatever
            for leftIndex in range(int(len(nums) / 2)):
                rightIndex = len(nums) - 1 - leftIndex
                nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
            return
                
        # shift digits after the reverse point
        leftIndex += 0
        nextPerm = False
        while leftIndex < len(nums) - 1:
            if nums[leftIndex] > nums[rightIndex]:
                nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
            elif rightIndex < len(nums):
                rightIndex += 1
            else:
                leftIndex += 1
                rightIndex = leftIndex + 1

            if rightIndex > len(nums) - 1:
                leftIndex += 1
                rightIndex = leftIndex + 1


def TestOutput(dat, sol):
    test = Solution()
    print(f"Before: {dat}")
    test.nextPermutation(dat)
    print(f"After:{dat}")
    assert(dat == sol)

def Test():
    # TestOutput([1,2],[2,1])

    # TestOutput([1,2,3], [1,3,2])

    # TestOutput([1,2,3, 4], [1,2,4,3])

    # TestOutput([1,2,3,5], [1,2,5,3])

    # TestOutput([1,5,4,3], [3,1,4,5])

    # TestOutput([5,4,3,1], [1,3,4,5])

    # TestOutput([4,3,1], [1,3,4])

    # TestOutput([1], [1])

    # TestOutput([1, 1], [1, 1])

    # TestOutput([1,3,2], [2,1,3])

    # TestOutput([5,4,7,5,3,2], [5,5,2,3,4,7])

    TestOutput([4,2,0,2,3,2,0], [4,2,0,3,0,2,2])

Test()


            
        