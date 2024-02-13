def convert_plaintext_to_ascii(text):
    """
    Convert plaintext into equivalent ASCII values.
    """
    ascii_values = []
    for char in text:
        ascii_values.append(ord(char))
    return ascii_values


def convert_ascii_to_hex(ascii_values):
    """
    Convert an array of ASCII values to hexadecimal representation.
    """
    hex_array = [hex(value)[2:].zfill(2) for value in ascii_values]
    return hex_array


def convert_hex_to_ascii(hex_string):
    """
    Convert a hexadecimal string to ASCII values.
    """
    return [int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)]
