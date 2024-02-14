import sys
sys.path.append('../') 


from helper.function import read_text_file, round_key
from helper.convert import convert_plaintext_to_ascii, convert_ascii_to_hex
from helper.create import create_initial_state_hex, create_initial_state_ascii, create_subkey_array, create_hex_to_ascii_matrix, create_ascii_to_hex_matrix
from encryption_operations.sub_bytes import  generate_sub_bytes
from encryption_operations.shift_rows import shift_rows
from encryption_operations.mix_columns import mix_columns





plaintext_file ="../data/plaintext.txt"
result_file = "../data/result.txt"
subkey_file = "../data/subkey_example.txt"
result_subkey_file = "../data/result_subkey.txt"





'''
Read a message from file “../data/plaintext.txt”, change each character into ASCII. 
After that,you should have 128 bits and obtain an initial state (check the example we mentioned in Lecture 5)
'''

plaintext_message = read_text_file(plaintext_file)

if plaintext_message: 
    print("plaintext_message\n", plaintext_message)

ascii_plaintext = convert_plaintext_to_ascii(plaintext_message)

if ascii_plaintext: 
    print("ascii_plaintext\n", ascii_plaintext)

hex_plaintext = convert_ascii_to_hex(ascii_plaintext)

if hex_plaintext:
    print("hex_plaintext\n", hex_plaintext)
 
initial_state_hex = create_initial_state_hex(hex_plaintext)
print("initial_state_hex\n", initial_state_hex)
initial_state_ascii = create_initial_state_ascii(ascii_plaintext)
print("initial_state_ascii\n", initial_state_ascii)




'''
Read the two subkeys from file “../data/subkey example.txt”, calculate one AddKey before Round
1 with subkey0. 
'''
subkeys_hex_string = create_subkey_array(read_text_file(subkey_file))
print("subkeys_hex_string\n", subkeys_hex_string)
subkey0_hex_string = subkeys_hex_string[0]
print("subkey0_hex_string\n", subkey0_hex_string)

subkey0_ascii_matrix = create_hex_to_ascii_matrix(subkey0_hex_string)
print("subkey0_ascii_matrix\n", subkey0_ascii_matrix)

subkey0_hex_matrix = create_ascii_to_hex_matrix(subkey0_ascii_matrix)
print("subkey0_hex_matrix\n", subkey0_hex_matrix)

add_round_key_ascii = round_key(initial_state_ascii, subkey0_ascii_matrix)
print("add_round_key_ascii\n", add_round_key_ascii) 

add_round_key_hex = create_ascii_to_hex_matrix(add_round_key_ascii)
print("add_round_key_hex\n", add_round_key_hex) 





'''
Compute operations in Round 1 (includes SubBytes, ShiftRows, MixColumns and one
AddKey with subkey1). The matrix for MixColumns can be found in Lecture 5, and how to perform
the corresponding multiplication over bytes can be found in Lecture 10
'''

'''
SubBytes
'''

ascii_state_after_subbytes = generate_sub_bytes(add_round_key_ascii) 
print("ascii_state_after_subbytes\n", ascii_state_after_subbytes) 
hex_state_after_subbytes = create_ascii_to_hex_matrix(ascii_state_after_subbytes)
print("hex_state_after_subbytes\n", hex_state_after_subbytes) 

'''
ShiftRows
'''

ascii_state_after_shiftrows = shift_rows(ascii_state_after_subbytes)
print("ascii_state_after_shiftrows\n", ascii_state_after_shiftrows)  
hex_state_after_shiftrows =  create_ascii_to_hex_matrix(ascii_state_after_shiftrows)
print("hex_state_after_shiftrows\n", hex_state_after_shiftrows)  

'''
MixColumns
'''

ascii_state_after_mixcolumns = mix_columns(ascii_state_after_shiftrows)
print("ascii_state_after_mixcolumns\n", ascii_state_after_mixcolumns)  
hex_state_after_mixcolumns = create_ascii_to_hex_matrix(ascii_state_after_mixcolumns)
print("hex_state_after_mixcolumns\n", hex_state_after_mixcolumns)  

'''
Another AddKey
'''

subkey1_hex_string = subkeys_hex_string[1]
subkey1_ascii_matrix = create_hex_to_ascii_matrix(subkey1_hex_string)
print("subkey1_ascii_matrix\n", subkey1_ascii_matrix)
subkey1_hex_matrix = create_ascii_to_hex_matrix(subkey1_ascii_matrix)
print("subkey1_hex_matrix\n", subkey1_hex_matrix)

add_round_key_ascii_1 = round_key(ascii_state_after_mixcolumns, subkey1_ascii_matrix)
print("add_round_key_ascii_1\n", add_round_key_ascii_1) 

add_round_key_hex_1 = create_ascii_to_hex_matrix(add_round_key_ascii_1)
print("add_round_key_hex_1\n", add_round_key_hex_1) 






'''
Print your result after the 1st round of AES encryption in terminal and write the result to a file
“../data/result.txt”. The result needs to be printed and written in hexadecimal.
'''
write_to_output = [
    "\nPlaintext Message: ",
    plaintext_message,
    "\nPlaintext converted to Hex: ",
    hex_plaintext,
    "\n\nStep 1: AddKey\n\n",
    "\nInitial State: ",
    initial_state_hex,
    "\nSubkeys in Hex: ",
    subkeys_hex_string,
    "\n0th subkey for 1st AddKey: ",
    subkey0_hex_string,
    "\nHex Matrix for Subkey 0: ",
    subkey0_hex_matrix,
    "\nResult of the 1st RoundKey: ",
    add_round_key_hex,
    "\n\nStep 2: Sub-Bytes\n\n",
    "\nHex after Sub-Bytes: ",
    hex_state_after_subbytes,
    "\n\n\nStep 3: ShiftRows\n\n",
    "\nHex after ShiftRows: ",
    hex_state_after_shiftrows,
    "\n\n\nStep 4: MixColumns\n\n",
    "\nHex after MixColumns: ",
    hex_state_after_mixcolumns,
    "\n\n\nStep 5: AddKey Part 2\n\n",
    "\nSubkey 1 Hex Matrix: ",
    subkey1_hex_matrix,
    "\n\n\n\n\nAfter RoundKey Hex Matrix (THIS IS THE FINAL ENCRYPTED VALUE.): ",
    add_round_key_hex_1
]


with open(result_file, "w") as file:
    for item in write_to_output:
        file.write(str(item) + "\n")






'''
Additional: 
Read the first subkey from file “../data/subkey example.txt”, generate the next subkey using sub-
key schedule algorithm in AES. Print the next subkey in terminal and write the result to a file
“../data/result_subkey.txt”. The result needs to be printed and written in hexadecimal.
'''

subkey0_hex_string = subkeys_hex_string[0]
