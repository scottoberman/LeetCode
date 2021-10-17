class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        self.s = s

        windWidth = 1
        windIndex = 0
        windS = ""
        longPal = ""
        lenS = len(self.s)

        # Process Rundown
        # 1. check if window contains palindrome
        # 2. if it does, extend max window width and move back to start
        # 3. else move window index over one
        # 4. terminate once window size becomes greater than string size

        windS = self.s[0]

        while len(longPal) + windIndex < lenS:
            if len(windS) > len(longPal) and self.isPalindrome(windS):
                longPal = windS

            if windIndex + windWidth < lenS:
                windS += self.s[windIndex + windWidth]
                windWidth += 1
            else:
                windIndex += 1
                windWidth = len(longPal)
                windS = self.s[windIndex : windIndex + windWidth]

        return longPal

    def isPalindrome(self, potentPal):
        LenPotentPal = len(potentPal)
        for x in range(0, len(potentPal)):
            if potentPal[x] != potentPal[LenPotentPal - x - 1]:
                return False
        return True


def Test():
    sol = Solution()
    #print("Longest palindrome: " + sol.longestPalindrome("asdf"))
    print("Longest palindrome: " + sol.longestPalindrome("aassaa"))
    print("Longest palindrome: " + sol.longestPalindrome("aassaaddddddddddddddddddddd"))
    print("Longest palindrome: " + sol.longestPalindrome("babad"))
    print("Longest palindrome: " + sol.longestPalindrome("zzzzxsaiowdjkjsdbfijasherjbasdfnasouierhaiwlefhasdofu9a8whriu3n908sdhvniw3nc08a8wnenfiauswuer09u34wkjfjsd09fuj2ij3 f90sdgjij32wnf09wrhgiun3098r34ntkjsdjg09sejrtiusje09tjdfgjjs0ed9rgu0s9drgzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxsaiowdjkjsdbfijasherjbasdfnasouierhaiwlefhasdofu9a8whriu3n908sdhvniw3nc08a8wnenfiauswuer09u34wkjfjsd09fuj2ij3 f90sdgjij32wnf09wrhgiun3098r34ntkjsdjg09sejrtiusje09tjdfgjjs0ed9rgu0s9drgzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxsaiowdjkjsdbfijasherjbasdfnasouierhaiwlefhasdofu9a8whriu3n908sdhvniw3nc08a8wnenfiauswuer09u34wkjfjsd09fuj2ij3 f90sdgjij32wnf09wrhgiun3098r34ntkjsdjg09sejrtiusje09tjdfgjjs0ed9rgu0s9drgzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxsaiowdjkjsdbfijasherjbasdfnasouierhaiwlefhasdofu9a8whriu3n908sdhvniw3nc08a8wnenfiauswuer09u34wkjfjsd09fuj2ij3 f90sdgjij32wnf09wrhgiun3098r34ntkjsdjg09sejrtiusje09tjdfgjjs0ed9rgu0s9drgzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"))

Test()
