import numpy as np


def gf_mul(a, b):
    """
    Galois Field (GF(2^8)) multiplication of two numbers.
    """
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1B  # AES irreducible polynomial
        b >>= 1
    return p

def mix_columns(state):
    """
    Mix columns of the state matrix using AES MixColumns operation.
    """
    polynomial_matrix = np.array(
        [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]], dtype=np.uint8
    )

    mixed_state = np.zeros_like(state)

    for i in range(4):
        for j in range(4):
            mixed_state[i][j] = (
                gf_mul(polynomial_matrix[i][0], state[0][j])
                ^ gf_mul(polynomial_matrix[i][1], state[1][j])
                ^ gf_mul(polynomial_matrix[i][2], state[2][j])
                ^ gf_mul(polynomial_matrix[i][3], state[3][j])
            )

    return mixed_state.tolist()
