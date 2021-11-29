from typing import List

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
                return True
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
test()