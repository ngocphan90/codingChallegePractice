def get_dups(array):
    ht = {}
    dups = []
    for x in array:
        if x in ht:
            dups.append(x)
        else:
            ht[x] = x
    return list(set(dups))

print (get_dups( [1,2,1,3,6,5]))