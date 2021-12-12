def compress( chars):
    output = ""
    counter = 0
    for index in range(0, len(chars)):
        if index == 0:
            output = str(chars[index])
            counter += 1
        else:
            if chars[index] == chars[index-1]:
                counter += 1
            else:
                output += str(chars[index])
                counter += 1
    for i in range(len(output)):
        print(output[i])







compress(["a","b","b","c","c","c"])