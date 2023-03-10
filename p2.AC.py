def generate_binary_code(message, probability_table):
    # Calculate the range for each symbol in the message
    ranges = []
    lower_bound = 0
    for symbol in message:
        upper_bound = lower_bound + probability_table[symbol]
        ranges.append((lower_bound, upper_bound))
        lower_bound = upper_bound
    # Encode the message by finding the binary representation of the final range
    code = ""
    for i in range(32):
        mid = (ranges[-1][0] + ranges[-1][1]) / 2
        if mid < 0.5:
            code += "0"
            ranges = [(ranges[-1][0] * 2, ranges[-1][1] * 2)]
        else:
            code += "1"
            ranges = [(2 * ranges[-1][0] - 1, 2 * ranges[-1][1] - 1)]
    return code

# Example usage
probability_table = {"a": 0.4, "b": 0.3, "c": 0.2, "d": 0.1}
message = "abcd"
binary_code = generate_binary_code(message, probability_table)
print(binary_code)
