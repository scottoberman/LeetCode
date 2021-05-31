/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize)
{
    int* sums = (int*)malloc(numsSize * sizeof(int));

    int sumCur = 0;
    for (int x = 0; x < numsSize; x++)
    {
        sumCur += nums[x];
        sums[x] = sumCur;
    }

    *returnSize = numsSize;

    return sums;
}


int main()
{
    int* testNums = (int*)malloc(sizeof(int) * 4);

    testNums[0] = 1;
    testNums[1] = 3;
    testNums[2] = 5;
    testNums[3] = 7;

    int returnSize = 0;

    runningSum(testNums, 4, returnSize);
}