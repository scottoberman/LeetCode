# Refactoring is not a bad idea.

from typing import List
from itertools import chain, combinations

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        # Key is the number, value is the frequency
        self.__freqsExpected = {}
        self.__depthTarget = n - 1
        self.__sums = sums
        
        depth = -1
        index = -1
        sumSoFar = self.__sums[0]
        
        self.__freqsExpected = freqsInit(self.__sums)
        potentialSol = []

        self.recurSearch(depth, index,sumSoFar, freqsInit(self.__sums), potentialSol)
        
        return potentialSol
        
        
    def recurSearch(self, depth, index, sumSoFar, freqs, potentialSol):
        haltSearch = False
        
        # Initial case (empty set)
        if index == -1:
            sumSoFar = 0

        # Short circuit a failure if the number is
        # not in numbers / has been removed.
        freqsNew = dict(freqs)
        if sumSoFar in freqsNew:
            freqsRemove(sumSoFar, freqsNew)
            if depth == self.__depthTarget:
                # Potential solution?
                return self.verifySolution(potentialSol)
            elif len(freqsNew) == 0:
                assert(False)
                # Not sure what this case entails
                return False
        else:
            return False
            
        while (not haltSearch) and \
        index + 1 < len(self.__sums):
            index += 1
            potentialSol.append(self.__sums[index])
            haltSearch = self.recurSearch(depth + 1, index, sumSoFar + self.__sums[index], freqsNew, potentialSol)
            if not haltSearch:
                potentialSol.pop()
            
        return haltSearch

    def verifySolution(self, sol):
        freqsSums = freqsInit(self.__sums)
        powerSetSol = self.powerSet(sol)

        setCur = next(powerSetSol)
        for x in range(len(self.__sums) - 1):
            sumCur = sum(setCur)
            if sumCur in freqsSums:
                freqsRemove(sumCur, freqsSums)
                setCur = next(powerSetSol)
            else:
                return False

        return True

    def powerSet(self, nums):
        s = list(nums)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
# Create dictionary of frequencies
def freqsInit(freqsOld):
    freqsNew = {}
    for x in freqsOld:
        if x in freqsNew:
            freqsNew[x] += 1
        else:
            freqsNew[x] = 1
    
    return freqsNew

# Mutator of freqs!
def freqsInsert(val, freqs):
    if val in freqs:
        freqs[val] += 1
    else:
        freqs[val] = 1
        
def freqsRemove(val, freqs):
    if val in freqs:
        freqs[val] -= 1
        if freqs[val] == 0:
            freqs.pop(val)
    else:
        # In our case, this sort of thing should be caught
        # before attempting a removal.
        assert False
     
def test():
    sol = Solution()
    
    res = sol.recoverArray(3, [-3,-2,-1,0,0,1,2,3])
    print(res)

    res = sol.recoverArray(2, [0,0,0,0])
    print(res)

    res = sol.recoverArray(4, [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8])
    print(res)

    res = sol.recoverArray(1, [0, 9])
    print(res)

    res = sol.recoverArray(3, [-574,-394,0,180,-180,-574,-754,0])
    print(res)

    res = sol.recoverArray(8, [-674,443,651,-731,-148,335,1143,479,878,-311,435,180,445,636,515,-391,397,224,536,1070,216,-727,388,-1046,913,615,1415,606,-627,-702,831,870,143,101,679,1214,23,1071,769,-67,1878,1849,-139,-18,1142,880,262,716,-201,1533,406,-177,750,244,659,726,898,343,-1190,1361,359,942,1705,-362,450,906,29,243,463,-530,215,-583,-1219,-221,-100,-192,836,52,253,-845,-684,-598,-219,24,980,999,1021,324,173,0,-248,167,798,414,562,1386,53,1487,-211,344,-38,-454,300,-645,-340,-292,-135,-247,-268,607,-484,1505,1677,-1075,-172,315,877,1648,-989,142,99,788,1078,-120,-218,927,1024,209,-412,1042,516,1107,-526,-91,644,287,-365,-321,1041,-655,72,1390,589,316,488,-57,1286,-419,144,-756,416,70,517,1242,291,1343,-383,630,444,-47,697,126,492,-563,851,-28,533,-1018,-21,152,415,587,680,1504,1458,-592,1185,507,271,1534,860,650,560,44,841,779,214,-501,486,-448,-875,-110,1113,823,-129,995,558,763,97,-336,286,1251,-846,-799,759,-75,1222,-164,951,-612,970,-254,487,-455,1734,1257,8,373,372,-239,196,-182,1314,-411,635,-382,123,-555,1050,706,907,677,171,172,-483,1189,15,807,687,734,368,-874,1304,1160,-283,9,794,1271,353,1333,-828,-20,306,-104,1114,245])
    print(res)

test()