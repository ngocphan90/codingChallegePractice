str = "Engineering"

print("Original string: " + str)

# Removing char at index 2
# using join() + list comprehension
res_str = ''.join([str[i] for i in range(len(str)) if i != 2])

print("String after removal of character: " + res_str)



