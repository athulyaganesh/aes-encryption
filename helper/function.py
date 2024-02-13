def read_text_file(file_path):
    """Reads the contents of a text file and returns it as a string."""
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    

def round_key(state, subkey):
    """
    Perform AddRoundKey operation on the state using the subkey.
    """
    for i in range(4):
        for j in range(4):
            state[i][j] ^= subkey[i][j]
    return state