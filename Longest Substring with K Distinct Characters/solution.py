def substring(string, maxOccur):
    start = 0
    occurs = {}
    maxLen = 0

    for end in range(len(string)):
        if string[end] not in occurs:
            occurs[string[end]] = 0
        
        occurs[string[end]] += 1
    
        while len(occurs) > maxOccur:
            occurs[string[start]] -= 1
            if occurs[string[start]] == 0:
                del occurs[string[start]]
            
            start += 1
    
        maxLen = max(maxLen, end - start + 1)

    return maxLen

print(substring("asdfff", 2))