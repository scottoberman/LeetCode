class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        rowStrs = ["" for x in range(numRows)]
        curRow = 0
        curCol = 0
        answer = s

        if numRows >= len(s):
            return answer

        for curChar in range(len(s)):
            if curCol % (numRows - 1) == 0:
                rowStrs[curRow] += (s[curChar])
                curRow = (curRow + 1) % numRows

                if curRow == 0:
                    curCol += 1

            else:
                curRow = numRows - (curChar % (numRows - 1) + 1)
                rowStrs[curRow] += (s[curChar])

                curCol += 1

                if curRow == 1:
                    curRow = 0

        answer = ""
        for rowStr in rowStrs:
            answer += rowStr

        return answer

    def printSol(self, rowStrs, numRows):
        for x in range(numRows - 1):
            print(rowStrs[x])


def Test():
    testy = Solution()

    numRows = 5
    s = "a"
    rowStrs = testy.convert("a", numRows)

    numRows = 2
    s = "a"
    rowStrs = testy.convert("a", numRows)

    numRows = 1
    s = "a"
    rowStrs = testy.convert("a", numRows)

    testy.printSol(rowStrs, numRows)

    print(rowStrs)

Test()