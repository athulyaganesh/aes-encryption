def plaintext_to_ascii(plaintext):
    ascii_values = []
    for char in plaintext:
        ascii_values.append(ord(char))
    return ascii_values
