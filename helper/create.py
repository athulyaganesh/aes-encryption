from numpy import transpose as numpy_transpose 
from numpy import reshape as numpy_reshape 

def create_initial_state_hex(hex):
    """
    Format hexadecimal values into a 2D array with columns of 4, transposed.
    """
    hex_matrix = [hex[i : i + 4] for i in range(0, len(hex), 4)]
    transposed_hex_matrix = [[row[i] for row in hex_matrix] for i in range(4)]
    return transposed_hex_matrix


def create_initial_state_ascii(ascii):
    # num_cols = 4
    # initial_state = [ascii[i:i+num_cols] for i in range(0, len(ascii), num_cols)]
    # return initial_state
    return numpy_transpose(numpy_reshape(ascii, (-1, 4)))


def create_subkey_array(subkeys_text):
    """
    Split the contents of the text file into two parts and create an array for each subkey value.
    """
    subkey_list = subkeys_text.strip().split('\n\n')
    subkey_arrays = []
    for subkey_text in subkey_list:
        subkey_array = [subkey for subkey in subkey_text.split()]
        subkey_arrays.extend(subkey_array)  # Extend the list instead of appending a sublist
    return subkey_arrays


def create_hex_to_ascii_matrix(hex_string):
    """
    Convert a hexadecimal string to a transposed 2D matrix of bytes.
    """
    matrix = []
    for i in range(0, 8, 2):
        column = [int(hex_string[j : j + 2], 16) for j in range(i, len(hex_string), 8)]
        matrix.append(column)
    return matrix
    # return numpy_transpose(numpy_reshape(arr, (-1, 4)))



def create_ascii_to_hex_matrix(matrix):
    """
    Convert a 4x4 matrix of ASCII integer values to a 4x4 matrix of hexadecimal strings.
    """
    hex_matrix = []
    for row in matrix:
        hex_row = ["{:02x}".format(byte) for byte in row]
        hex_matrix.append(hex_row)
    return hex_matrix

