def compress(data):
    # Initialize variables
    compressed_data = []
    search_buffer = ""
    lookahead_buffer = ""
    
    # Set the size of the search buffer and lookahead buffer
    search_buffer_size = 10
    lookahead_buffer_size = 5
    
    # Iterate through the data, one character at a time
    for i in range(len(data)):
        # Add the current character to the lookahead buffer
        lookahead_buffer += data[i]
        
        # If the lookahead buffer is full, or if we have reached the end of the data
        if len(lookahead_buffer) == lookahead_buffer_size or i == len(data) - 1:
            # Find the longest matching string in the search buffer
            best_match_length = 0
            best_match_position = 0
            for j in range(len(search_buffer)):
                # Check if the current substring in the search buffer matches the lookahead buffer
                match_length = 0
                for k in range(len(lookahead_buffer)):
                    if search_buffer[j+k] != lookahead_buffer[k]:
                        break
                    match_length += 1
                
                # Update the best match if necessary
                if match_length > best_match_length:
                    best_match_length = match_length
                    best_match_position = j
            
            # Add the best match to the compressed data
            compressed_data.append((best_match_position, best_match_length, lookahead_buffer[best_match_length:]))
            
            # Update the search buffer
            search_buffer += lookahead_buffer
            search_buffer = search_buffer[-search_buffer_size:]
            
            # Clear the lookahead buffer
            lookahead_buffer = ""
    
    return compressed_data

def decompress(compressed_data):
    # Initialize variables
    decompressed_data = ""
    search_buffer = ""
    
    # Iterate through the compressed data
    for i in range(len(compressed_data)):
        # Get the current match position, length, and character
        match_position, match_length, c = compressed_data[i]
        
        # Add the matching substring from the search buffer to the decompressed data
        decompressed_data += search_buffer[match_position:match_position+match_length]
        
        # Add the new character to the search buffer and the decompressed data
        search_buffer += c
        decompressed_data += c
    
    return decompressed_data

# Test the LZ77 implementation
data = "ABCDEFABCRDEDDFHTFDDD"
compressed_data = compress(data)
print(compressed_data)
decompressed_data = decompress(compressed_data)
print(decompressed_data)