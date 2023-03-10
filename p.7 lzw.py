def lzw_compress(text):
    dictionary = {chr(i): i for i in range(256)}
    next_index = 256
    result = []
    i = 0
    while i < len(text):
        j = 1
        while j <= len(text) - i:
            if text[i:i+j] in dictionary:
                j += 1
            else:
                break
        index = dictionary.get(text[i:i+j-1], None)
        if index is None:
            index = ord(text[i])
        result.append(index)
        dictionary[text[i:i+j]] = next_index
        next_index += 1
        i += j - 1
    return result

def lzw_decompress(compressed):
    dictionary = {i: chr(i) for i in range(256)}
    next_index = 256
    result = ""
    string = chr(compressed[0])
    result += string
    for index in compressed[1:]:
        if index in dictionary:
            next_string = dictionary[index]
        elif index == next_index:
            next_string = string + string[0]
        else:
            raise ValueError("Compressed data is corrupted")
        result += next_string
        dictionary[next_index] = string + next_string[0]
        next_index += 1
        string = next_string
    return result

text = "MISSISSIPI"
compressed = lzw_compress(text)
print("\nCompressed:")
print(compressed)
print("\nDecompressed:")
print(lzw_decompress(compressed))
