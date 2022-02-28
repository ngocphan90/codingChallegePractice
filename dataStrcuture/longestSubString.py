
def lengthOfLongestSubstring(s) -> int:
    hashmap = {}
    longest, left, right = 0,0,0
    for right, char in enumerate(s):
        if char in hashmap:
            sum = hashmap[char]
            if sum > left:
                left = sum + 1

        longest = max(longest, right - left + 1)

        hashmap[char] = right
    return longest


print(lengthOfLongestSubstring("abcabd"))