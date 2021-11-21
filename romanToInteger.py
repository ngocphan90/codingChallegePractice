# create a hashmap


values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def romanToInt(s: str) :
    total = 0
    i = 0
    # loop through the string
    while i < len(s):
        if i + 1 < len(s) and values[s[i+1]] > values[s[i]]:
            total += values[s[i+1]] - values[s[i]]
            i += 2

        else:
            total += values[s[i]]
            i += 1
    return total

print(romanToInt("XIV"))