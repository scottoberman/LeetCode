import time

class Window:
    def __init__(self) -> None:
        self.width = 1
        self.index = 0
class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        self.s = s

        wind = Window

        wind.width = 1
        wind.index = 0
        longPal = ""
        lenS = len(self.s)
        palInCurWindow = False

        # Process Rundown
        # 1. check if window contains palindrome
        # 2. if it does, extend max window width 
        # 3. else move window index over one
        # 4. terminate once window size becomes greater than string size

        while len(longPal) + wind.index < lenS:
            if wind.width > len(longPal) and self.isPalindrome(s, wind):
                longPal = self.s[wind.index: wind.index + wind.width]


            if wind.index + wind.width < lenS:
                wind.width += 1

            else:
                wind.index += 1
                wind.width = len(longPal)


        return longPal

    def isPalindrome(self, s, wind):
        upperBound = wind.index + wind.width - 1
        for x in range(wind.index, upperBound):
            if s[x] != s[upperBound - x]:
                return False
        return True


def Test():
    timeStart = time.time()
    sol = Solution()
    #print("Longest palindrome: " + sol.longestPalindrome("asdf"))
    print("Longest palindrome: " + sol.longestPalindrome("aassaa"))
    print("Longest palindrome: " + sol.longestPalindrome("aassaaddddddddddddddddddddd"))
    print("Longest palindrome: " + sol.longestPalindrome("babad"))
    print("Longest palindrome: " + sol.longestPalindrome("zzzzxsaiowdjkjsdbfijasherjbasdfnasouierhaiwlefhasdofu9a8whriu3n908sdhvniw3nc08a8wnenfiauswuer09u34wkjfjsd09fuj2ij3 f90sdgjij32wnf09wrhgiun3098r34ntkjsdjg09sejrtiusje09tjdfgjjs0ed9rgu0s9drgzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxsaiowdjkjsdbfijasherjbasdfnasouierhaiwlefhasdofu9a8whriu3n908sdhvniw3nc08a8wnenfiauswuer09u34wkjfjsd09fuj2ij3 f90sdgjij32wnf09wrhgiun3098r34ntkjsdjg09sejrtiusje09tjdfgjjs0ed9rgu0s9drgzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxsaiowdjkjsdbfijasherjbasdfnasouierhaiwlefhasdofu9a8whriu3n908sdhvniw3nc08a8wnenfiauswuer09u34wkjfjsd09fuj2ij3 f90sdgjij32wnf09wrhgiun3098r34ntkjsdjg09sejrtiusje09tjdfgjjs0ed9rgu0s9drgzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxsaiowdjkjsdbfijasherjbasdfnasouierhaiwlefhasdofu9a8whriu3n908sdhvniw3nc08a8wnenfiauswuer09u34wkjfjsd09fuj2ij3 f90sdgjij32wnf09wrhgiun3098r34ntkjsdjg09sejrtiusje09tjdfgjjs0ed9rgu0s9drgzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"))


Test()
