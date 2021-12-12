#Given an input list of strings, for each letter appearing anywhere
#in the list, find the other letter(s) that appear in the most
#number of words with that letter.
#['abc', 'bcd', 'cde'] = >
#{
#    a: [b, c],  # b appears in 1 word with a, c appears in 1 word with a
#    b: [c],  # c appears in 2 words with b, a and d each appear in only 1 word with b
#    c: [b, d],  # b appears in 2 words with c, d appears in 2 words with c. But a and e each
#    appear in only 1 word
#with c.
#        d: [c],  # c appears in 2 words with d. But b and e each appear in only 1 word with d
#           e: [c, d],  # c appears in 1 word with e, d appears in 1 word with e
import collections
import string


def a(c):
    cnt = collections.defaultdict(dict)
    arr = ["abef", "bcd", "bde", "cadf"]

    for word in arr:
        for i, c in enumerate(word):
            adj1 = word[i - 1]
            cnt[c][adj1] = cnt[c].get(adj1, 0) + 1
            adj2 = word[(i + 1) % len(word)]
            cnt[c][adj2] = cnt[c].get(adj2, 0) + 1

            adj3 = word[(i + 2) % len(word)]
            cnt[c][adj3] = cnt[c].get(adj3, 0) + 1

    for c in string.ascii_letters:
        if cnt[c]:
            mx = max(cnt[c].values())
            print("adjacent characters with most count for", c, [k for k, v in cnt[c].items() if v == mx])



print(a([]))