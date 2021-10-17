class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        windWidth = 1
        windIndex = 0
        windS = ""
        longPal = ""

        # Process Rundown
        # 1. check if window contains palindrome
        # 2. if it does, extend max window width and move back to start
        # 3. else move window index over one
        # 4. terminate once window size becomes greater than string size

        windS = s[0]

        while len(longPal) + windIndex < len(s):
            if self.isPalindrome(windS):
                longPal = windS

            if windIndex + windWidth < len(s):
                windS += s[windIndex + windWidth]
                windWidth += 1
            else:
                windIndex += 1
                windWidth = len(longPal)
                windS = s[windIndex : windIndex + windWidth]

        return longPal

    def isPalindrome(self, s):
        sBackwards = s[::-1]
        return len(s) > 0 and s == sBackwards


def Test():
    sol = Solution()
    #print("Longest palindrome: " + sol.longestPalindrome("asdf"))
    print("Longest palindrome: " + sol.longestPalindrome("aassaa"))
    print("Longest palindrome: " + sol.longestPalindrome("aassaaddddddddddddddddddddd"))
    print("Longest palindrome: " + sol.longestPalindrome("babad"))

Test()
