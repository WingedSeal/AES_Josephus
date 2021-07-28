import random
import pandas as pd
from tqdm import tqdm
from .utils import random_string, string_to_hex 
from .encryptdecrypt import encrypt, decrypt
from .mode import Mode

def string_to_binary(string: str) -> str:
    return ''.join(f'{ord(char):08b}' for char in string)
def avalanche(string1: str,string2: str) -> float:
    if len(string1) != len(string2): 
        raise ValueError(f"Strings' length does not match ({len(string1)}, {len(string2)})")
    return hamming_distance(string1,string2)/len(string_to_binary(string1))
def hamming_distance(string1: str, string2: str) -> int:
    return sum(char1 != char2 for char1, char2 in zip(string_to_binary(string1), string_to_binary(string2)))

def alter_char_in_string(string: str, str_length: int) -> str:
    altered_string = list(string)
    char_index = random.randrange(str_length)
    altered_string[char_index] = random_string(1, excluded=string[char_index])
    return ''.join(altered_string)

def avalanche_df(row: int) -> pd.DataFrame:
    cipherkey = random_string(16)
    avalanche_array = []
    for _ in tqdm(range(row)):
        plaintext1 = random_string(16)
        plaintext2 = alter_char_in_string(plaintext1, 16)
        aes_encrypted1 = encrypt(plaintext1, cipherkey, mode=Mode.ORIGINAL).to_string()
        aes_encrypted2 = encrypt(plaintext2, cipherkey, mode=Mode.ORIGINAL).to_string()
        josephus_encrypted1 = encrypt(plaintext1, cipherkey, mode=Mode.JOSEPHUS).to_string()
        josephus_encrypted2 = encrypt(plaintext2, cipherkey, mode=Mode.JOSEPHUS).to_string()
        modified_aes_encrypted1 = encrypt(plaintext1, cipherkey, mode=Mode.MODIFIED_ORIGINAL).to_string()
        modified_aes_encrypted2 = encrypt(plaintext2, cipherkey, mode=Mode.MODIFIED_ORIGINAL).to_string()
        aes_avalanche_value = avalanche(aes_encrypted1, aes_encrypted2)
        josephus_avalanche_value = avalanche(josephus_encrypted1, josephus_encrypted2)
        modified_aes_avalanche_value = avalanche(modified_aes_encrypted1, modified_aes_encrypted2)

        avalanche_array.append([
            plaintext1, 
            plaintext2, 
            string_to_hex(aes_encrypted1), 
            string_to_hex(aes_encrypted2), 
            aes_avalanche_value, 
            string_to_hex(josephus_encrypted1), 
            string_to_hex(josephus_encrypted2), 
            josephus_avalanche_value,
            string_to_hex(modified_aes_encrypted1),
            string_to_hex(modified_aes_encrypted2),
            modified_aes_avalanche_value
            ])

    avalanche_df = pd.DataFrame(avalanche_array, columns=[
        "Plaintext_1", 
        "Plaintext_2", 
        "Original_AES_Ciphertext_1", 
        "Original_AES_Ciphertext_2", 
        "Original_AES_Avalanche", 
        "Josephus_AES_Ciphertext_1", 
        "Josephus_AES_Ciphertext_2", 
        "Josephus_AES_Avalanche",
        "Modified_AES_Ciphertext_1", 
        "Modified_AES_Ciphertext_2", 
        "Modified_AES_Avalanche"])
        
    return avalanche_df
