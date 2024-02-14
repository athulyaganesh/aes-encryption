def read_text_file(file_path):
    """Reads the contents of a text file and returns it as a string."""
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

def round_key(initial_state, subkey):
    """
    Perform AddRoundKey operation on the state using the subkey.
    """
    result = []

    for i in range(len(initial_state)):
        row = []
        for j in range(len(initial_state[i])):
            xor_result = initial_state[i][j] ^ subkey[i][j]
            row.append(xor_result)
        result.append(row)

    return result