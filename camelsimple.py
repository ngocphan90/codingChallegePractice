class Solution:
    def solve(self, words):
        s = "".join(word[0].upper() + word[1:].lower() for word in words)
        return s[0].lower() + s[1:]


ob = Solution()
words = ["hello", "world", "python", "programming"]
print(ob.solve(words))
