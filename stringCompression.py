def compress( chars):
    output = ""
    counter = 0
    for index in range(0, len(chars)):
        if index == 0:
            output = (chars[index])
            counter += 1
        else:
            if chars[index] == chars[index-1]:
                counter += 1
            else:
                if counter != 1:
                    output += str(counter)

                output += (chars[index])
                counter = 1
    if counter != 1:
        output += str(counter)

    for i in range(len(output)):
        chars[i] = output[i]
        print(chars[i])
    print(chars)
    return len(output)


(compress(["a","b","b","c","c","c"]))