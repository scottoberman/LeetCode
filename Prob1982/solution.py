from typing import List

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        # Key is the number, value is the frequency
        self.__freqsExpected = {}
        self.__depthTarget = n - 1
        self.__sums = sums
        
        depth = 0
        index = 0
        
        self.__freqsExpected = freqsInit(self.__sums)
        
        self.recurSearch(depth, index, freqsInit(self.__sums))
        
        
    def recurSearch(self, depth, index, freqs):
        sumFound = False
        if depth == self.__depthTarget:
            return freqs == self.__freqsExpected
        else:
            # Short circuit a failure if the number is
            # not in numbers / has been removed.
            if not self.__sums[index] in freqs:
                return False
            else:
                freqsNew = freqsInit(freqs)
                freqsRemove(self.__sums[index], freqsNew)
                depth += 1
                while not sumFound and \
                depth + index < len(self.__sums) - self.__depthTarget:
                    index += 1
                    sumFound = self.recurSearch(depth, index, freqsNew)

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
    else:
        # In our case, this sort of thing should be caught
        # before attempting a removal.
        assert False
     
def test():
    sol = Solution()
    
    res = sol.recoverArray(3, [-3,-2,-1,0,0,1,2,3])
    print(res)
                
test()