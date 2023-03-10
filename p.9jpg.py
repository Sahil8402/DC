from heapq import heappush, heappop, heapify
from collections import defaultdict
import numpy as np


def huffman_encoding(arr):
    # convert 8x8 matrix into 64 element list
    arr_list = arr.flatten().tolist()

    # calculate frequency of each element in the list
    freq = defaultdict(int)
    for symbol in arr_list:
        freq[symbol] += 1

    # build huffman tree
    heap = [[wt, [sym, ""]] for sym, wt in freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # create dictionary of huffman codes
    huffman_dict = dict(heappop(heap)[1:])

    # encode the input list using the huffman codes
    encoded_list = [huffman_dict[symbol] for symbol in arr_list]
    encoded_str = "".join(encoded_list)

    return encoded_str, huffman_dict


def huffman_decoding(encoded_str, huffman_dict):
    # create reverse dictionary of huffman codes
    reverse_dict = {v: k for k, v in huffman_dict.items()}

    # decode the encoded string using the reverse dictionary
    code = ""
    decoded_list = []
    for bit in encoded_str:
        code += bit
        if code in reverse_dict:
            symbol = reverse_dict[code]
            decoded_list.append(symbol)
            code = ""

    # convert the decoded list into 8x8 matrix
    decoded_arr = np.array(decoded_list).reshape((8, 8))

    return decoded_arr


# input 8x8 matrix
arr = np.array([[52, 55, 61, 66, 70, 61, 64, 73],
                [63, 59, 55, 90, 109, 85, 69, 72],
                [62, 59, 68, 113, 144, 104, 66, 73],
                [63, 58, 71, 122, 154, 106, 70, 69],
                [67, 61, 68, 104, 126, 88, 68, 70],
                [79, 65, 60, 70, 77, 68, 58, 75],
                [85, 71, 64, 59, 55, 61, 65, 83],
                [87, 79, 69, 68, 65, 76, 78, 94]])

# encode and compress the matrix using huffman coding
encoded_str, huffman_dict = huffman_encoding(arr)

# print the encoded string and huffman dictionary
print("Encoded String:\n", encoded_str)
print("Huffman Dictionary:\n", huffman_dict)

# decode and decompress the encoded string using huffman coding
decoded_arr = huffman_decoding(encoded_str, huffman_dict)
print("Decoded Array:\n", decoded_arr)
