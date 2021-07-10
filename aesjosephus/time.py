from aesjosephus import encrypt, decrypt
from aesjosephus.utils import random_string

from time import time
from typing import Tuple, Any, Callable
import pandas as pd

def record_time(func: Callable) -> Tuple[Any, int]:
    def wrapper(*args, **kwargs):
        time_used = 0
        while time_used==0:
            start_time = time()
            return_value = func(*args, **kwargs)
            time_used = time()-start_time
        return return_value, time_used
    return wrapper

@record_time
def encrypt_normal(plaintext, cipherkey):
    return encrypt(plaintext,cipherkey,mode="normal").to_string()

@record_time
def encrypt_josephus(plaintext, cipherkey):
    return encrypt(plaintext,cipherkey,mode="josephus").to_string()

@record_time
def encrypt_modified(plaintext, cipherkey):
    return encrypt(plaintext,cipherkey,mode="modified").to_string()

@record_time
def decrypt_normal(ciphertext, cipherkey):
    return decrypt(ciphertext,cipherkey,mode="normal").to_string()

@record_time
def decrypt_josephus(ciphertext, cipherkey):
    return decrypt(ciphertext,cipherkey,mode="josephus").to_string()

@record_time
def decrypt_modified(ciphertext, cipherkey):
    return decrypt(ciphertext,cipherkey,mode="modified").to_string()



def time_df(row: int) -> pd.DataFrame:
    cipherkey = random_string(16)
    time_array = []
    for _ in range(row):
        plaintext = random_string(16)
        aes_encrypted,  aes_encryption_time = encrypt_normal(plaintext, cipherkey)
        josephus_encrypted, josephus_encryption_time = encrypt_josephus(plaintext, cipherkey)
        modified_aes_encrypted, modified_aes_encryption_time = encrypt_modified(plaintext, cipherkey)
        _, aes_decryption_time = decrypt_normal(aes_encrypted, cipherkey)
        _, josephus_decryption_time = decrypt_josephus(josephus_encrypted, cipherkey)
        _, modified_aes_decryption_time = decrypt_modified(modified_aes_encrypted, cipherkey)
        time_array.append([
            aes_encryption_time, 
            aes_decryption_time, 
            josephus_encryption_time, 
            josephus_decryption_time,
            modified_aes_encryption_time,
            modified_aes_decryption_time])
    time_df = pd.DataFrame(time_array, columns=[
        "Original_AES_Encryption_Time", 
        "Original_AES_Decryption_Time", 
        "Josephus_AES_Encryption_Time", 
        "Josephus_AES_Decryption_Time",
        "Modified_AES_Encryption_Time", 
        "Modified_AES_Decryption_Time"])
    return time_df
