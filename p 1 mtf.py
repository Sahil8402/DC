def search(input_char, char_list):
    # Returns the index at which the input character exists in the list
    for i in range(len(char_list)):
        if char_list[i] == input_char:
            return i

def move_to_front(curr_index, char_list):
    # Takes curr_index of input_char as argument
    # to bring that character to the front of the list
    char = char_list.pop(curr_index)
    char_list.insert(0, char)

def mtf_encode(input_text, char_list):
    # Move-to-Front Encoding
    output_arr = []

    for char in input_text:
        # Linear Searches the characters of input_text in list
        output_arr.append(search(char, char_list))

        # Moves the searched character to the front of the list
        move_to_front(output_arr[-1], char_list)

    return output_arr

# Driver program to test functions above
if __name__ == '__main__':
    input_text = "panama"
    char_list = list("abcdefghijklmnopqrstuvwxyz")

    print(f"Input text: {input_text}")
    print("Move to Front Transform:", end=" ")

    # Computes Move to Front transform of given text
    mtf_transform = mtf_encode(input_text, char_list)
    print(mtf_transform)
