import sys
sys.path.append('../') 

from helper.function import read_text_file, round_key
from helper.convert import convert_plaintext_to_ascii, convert_ascii_to_hex
from helper.create import create_initial_state_hex, create_initial_state_ascii, create_subkey_array, create_hex_to_ascii_matrix, create_ascii_to_hex_matrix
from operations.sub_bytes import  generate_sub_bytes

plaintext_file = "../data/plaintext.txt"
result_file = "../data/result.txt"
subkey_file = "../data/subkey_example.txt"



'''
Read a message from file “../data/plaintext.txt”, change each character into ASCII. 
After that,you should have 128 bits and obtain an initial state (check the example we mentioned in Lecture 5)
'''

plaintext_message = read_text_file(plaintext_file)

if plaintext_message: 
    print("plaintext_message ", plaintext_message)

ascii_plaintext = convert_plaintext_to_ascii(plaintext_message)

if ascii_plaintext: 
    print("ascii_plaintext ", ascii_plaintext)

hex_plaintext = convert_ascii_to_hex(ascii_plaintext)

if hex_plaintext:
    print("hex_plaintext ", hex_plaintext)
 
initial_state_hex = create_initial_state_hex(hex_plaintext)
initial_state_ascii = create_initial_state_ascii(ascii_plaintext)

print("initial_state_hex ", initial_state_hex)
print("initial_state_ascii ", initial_state_ascii)



'''
Read the two subkeys from file “../data/subkey example.txt”, calculate one AddKey before Round
1 with subkey0. 
'''
subkeys_hex_string = create_subkey_array(read_text_file(subkey_file))
print("subkeys_hex_string ", subkeys_hex_string)
subkey0_hex_string = subkeys_hex_string[0]
print("subkey0_hex_string ", subkey0_hex_string)

subkey0_ascii_matrix = create_hex_to_ascii_matrix(subkey0_hex_string)
print("subkey0_ascii_matrix ", subkey0_ascii_matrix)

subkey0_hex_matrix = create_ascii_to_hex_matrix(subkey0_ascii_matrix)
print("subkey0_hex_matrix ", subkey0_hex_matrix)

add_round_key_ascii = round_key(initial_state_ascii, subkey0_ascii_matrix)
print("add_round_key_ascii ", add_round_key_ascii) 

add_round_key_hex = create_ascii_to_hex_matrix(add_round_key_ascii)
print("add_round_key_hex ", add_round_key_hex) 



'''
Compute operations in Round 1 (includes SubBytes, ShiftRows, MixColumns and one
AddKey with subkey1). The matrix for MixColumns can be found in Lecture 5, and how to perform
the corresponding multiplication over bytes can be found in Lecture 10
'''


'''
SubBytes
'''

ascii_state_after_subbytes = generate_sub_bytes(add_round_key_ascii) 
print("ascii_state_after_subbytes ", ascii_state_after_subbytes) 
hex_state_after_subbytes = create_ascii_to_hex_matrix(ascii_state_after_subbytes)
print("hex_state_after_subbytes ", hex_state_after_subbytes) 

'''
ShiftRows
'''

'''
MixColumns
'''

'''
Another AddKey
'''

'''
Print your result after the 1st round of AES encryption in terminal and write the result to a file
“../data/result.txt”. The result needs to be printed and written in hexadecimal.
'''

'''
Additional: 
Read the first subkey from file “../data/subkey example.txt”, generate the next subkey using sub-
key schedule algorithm in AES. Print the next subkey in terminal and write the result to a file
“../data/result subkey.txt”. The result needs to be printed and written in hexadecimal.
'''