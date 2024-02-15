# AES Encryption - Round 1 Implementation

This project implements the first round of encryption in the Advanced Encryption Standard (AES) algorithm. Given a 128-bit message, two subkeys `subkey0` and `subkey1`, the program performs one AddKey operation before Round 1 and the corresponding operations (SubBytes, ShiftRows, MixColumns, and AddKey) in Round 1. The output of the encryption after Round 1 is then provided.

## Functionality

The program provides the following functionality:

- **AddKey Operation**: Adds the input message with `subkey0` before Round 1.

- **SubBytes Operation**: Substitutes each byte of the state matrix with a corresponding byte from the S-box.

- **ShiftRows Operation**: Performs a cyclic left shift on each row of the state matrix.

- **MixColumns Operation**: Applies a matrix multiplication to each column of the state matrix.

- **Subkey Generation**: Given a 128-bit encryption key, the program generates the first two subkeys (`subkey0` and `subkey1`) according to the subkey schedule algorithm.

## Usage

To use the program:

To run as it, please run the command "python3 main.py" within the src directory.

3. Input the message to be encrypted in data/plaintext.txt.
4. Perform one AddKey operation with `subkey0`.
5. Execute the SubBytes, ShiftRows, and MixColumns operations in Round 1.
6. Perform one AddKey operation with `subkey1`.
7. Output the encrypted message after Round 1.

For the additional task, 

1. Provide 2 128-bit encryption key in the data/subkey_example.txt file.
2. Generate the first two subkeys (`subkey0` and `subkey1`) using the provided key.

## Assumptions

- The S-box used in the SubBytes operation is assumed to be provided.
- An encryption key has exactly 128 bits in this implementation.

## Subkey Schedule Algorithm

The subkey schedule algorithm is used to generate a series of subkeys from the original encryption key. These subkeys are used in each round of the AES encryption process. In this project, the first two subkeys (`subkey0` and `subkey1`) are generated based on the provided encryption key.

## Contributors

This project is implemented by Athulya Ganesh. 