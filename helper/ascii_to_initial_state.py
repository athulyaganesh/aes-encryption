def ascii_to_matrix(ascii_values):
    matrix = [[0] * 4 for _ in range(4)]  # Initialize a 4x4 matrix with zeros
    for i, value in enumerate(ascii_values):
        row = i % 4
        col = i // 4
        matrix[row][col] = value
    return matrix