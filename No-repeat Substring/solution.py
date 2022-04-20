def NoRep(string):
    indStart = 0
    occurs = {}
    lenMax = 0
    indEndBest = 0;
    indStartBest = 0

    for indEnd in range(len(string)):
        if string[indEnd] in occurs:
            occurs[string[indEnd]] += 1
        else:
            occurs[string[indEnd]] = 1

        while occurs[string[indEnd]] > 1:
            if occurs[string[indStart]] > 1:
                occurs[string[indStart]] -= 1
            else:
                del occurs[string[indStart]]

            indStart += 1
        
        lenMaxOg = lenMax
        lenMax = max(lenMax, indEnd - indStart + 1)
        if lenMax != lenMaxOg:
            indEndBest = indEnd
            indStartBest = indStart

    return string[indStartBest:indEndBest + 1], lenMax
print(NoRep("asdf"))
print(NoRep("asdffqwertyui"))



