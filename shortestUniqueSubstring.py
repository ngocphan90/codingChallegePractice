# Given an input list of names, for each name, find the shortest substring that only appears in that name.
# Input: ["cheapair", "cheapoair", "peloton", "pelican"]
# Output:
# "cheapair": "pa"  // every other 1-2 length substring overlaps with cheapoair
# "cheapoair": "po" // "oa" would also be acceptable
# "pelican": "ca"   // "li", "ic", or "an" would also be acceptable
# "peloton": "t"    // this single letter doesn't occur in any other string


import collections
import string


def a(a):
    result = collections.defaultdict(dict)
    arr = ["pal", "poo"]
    #using hashmap to put each string into map
    for st in arr:
        result[st] = st
        for i in range(0, len(st)):
            for j in range(i+1, len(st)):
                subStr = (st[i:j])
                addSub = True
                for st2 in arr:
                    if st2 == st:
                        continue
                    if subStr in st2:
                        addSub = False
                        break
                if addSub and len(subStr) < len(result.get(st)):
                    result[st] = subStr


    return result


print(a([]))

