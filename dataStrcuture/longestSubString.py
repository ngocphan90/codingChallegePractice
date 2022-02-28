
def lengthOfLongestSubstring(s) -> int:
    hashmap = {}
    longest, left, right = 0,0,0
    for right in range(len(s)):
        r= s[right]
        if r not in hashmap:
            hashmap[r] = right
            prevSeenChar = hashmap[r]
        else:
            left = prevSeenChar + 1
            right += 1
        longest = max(longest, right - left +1)

    return longest


print(lengthOfLongestSubstring("abcdacd"))