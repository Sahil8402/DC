import heapq

class Node:
    def __init__(self, symbol, frequency, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.frequency == other.frequency:
            return id(self) < id(other)
        return self.frequency < other.frequency

def build_frequency_table(data):
    frequency_table = {}
    for symbol in data:
        if symbol not in frequency_table:
            frequency_table[symbol] = 0
        frequency_table[symbol] += 1
    return frequency_table

def build_huffman_tree(frequency_table):
    heap = []
    for symbol, frequency in frequency_table.items():
        heap.append(Node(symbol, frequency))
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        node = Node(None, left.frequency + right.frequency, left, right)
        heapq.heappush(heap, node)
    return heap[0]

def build_codewords(node, codewords, prefix):
    if node is None:
        return
    if node.symbol is not None:
        codewords[node.symbol] = prefix
    build_codewords(node.left, codewords, prefix + "0")
    build_codewords(node.right, codewords, prefix + "1")

def compress(data):
    frequency_table = build_frequency_table(data)
    huffman_tree = build_huffman_tree(frequency_table)
    codewords = {}
    build_codewords(huffman_tree, codewords, "")
    compressed_data = ""
    for symbol in data:
        compressed_data += codewords[symbol]
    return compressed_data, huffman_tree, frequency_table

def decompress(compressed_data, huffman_tree, frequency_table):
    data = ""
    node = huffman_tree
    for bit in compressed_data:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.symbol is not None:
            data += node.symbol
            node = huffman_tree
    return data

def main():
    data = "Hello Radhey Mugdal here"
    compressed_data, huffman_tree, frequency_table = compress(data)
    print("Original data:", data)
    print("Compressed data:", compressed_data)
    decompressed_data = decompress(compressed_data, huffman_tree, frequency_table)
    print("Decompressed data:", decompressed_data)

if __name__ == "__main__":
    main()
