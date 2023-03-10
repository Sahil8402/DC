def lz78_compress(text):
    dictionary = {char: idx for idx, char in enumerate(set(text))}
    result = []
    i = 0
    while i < len(text):
        j = i + 1
        while j <= len(text) and text[i:j] in dictionary:
            j += 1
        if j > len(text):
            break
        dictionary[text[i:j]] = len(dictionary) + 1
        result.append((dictionary[text[i:j - 1]], text[j - 1]))
        i = j
    return result

def lz78_decompress(compressed):
    dictionary = {idx: char for idx, char in enumerate(set(text))}
    result = ""
    for code, next_char in compressed:
        if code in dictionary:
            result += dictionary[code] + next_char
            dictionary[len(dictionary) + 1] = dictionary[code] + next_char
        else:
            result += next_char
            dictionary[len(dictionary) + 1] = next_char
    return result

text = "MISSISSIPI"
compressed = lz78_compress(text)
print("\nCompressed:")
print(compressed)
print("\nDecompressed:")
print(lz78_decompress(compressed))
