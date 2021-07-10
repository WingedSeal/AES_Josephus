from .mode import Mode
from .encryptdecrypt import encrypt, decrypt
from .utils import random_string

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
def timed_encrypt(plaintext, cipherkey, mode):
    return encrypt(plaintext,cipherkey, mode).to_string()

@record_time
def timed_decrypt(ciphertext, cipherkey, mode):
    return decrypt(ciphertext,cipherkey,mode).to_string()



def time_df(row: int) -> pd.DataFrame:
    cipherkey = random_string(16)
    time_array = []
    for _ in range(row):
        plaintext = random_string(16)
        aes_encrypted,  aes_encryption_time = timed_encrypt(plaintext, cipherkey, Mode.ORIGINAL)
        josephus_encrypted, josephus_encryption_time = timed_encrypt(plaintext, cipherkey, Mode.JOSEPHUS)
        modified_aes_encrypted, modified_aes_encryption_time = timed_encrypt(plaintext, cipherkey, Mode.MODIFIED_ORIGINAL)
        _, aes_decryption_time = timed_decrypt(aes_encrypted, cipherkey, Mode.ORIGINAL)
        _, josephus_decryption_time = timed_decrypt(josephus_encrypted, cipherkey, Mode.JOSEPHUS)
        _, modified_aes_decryption_time = timed_decrypt(modified_aes_encrypted, cipherkey, Mode.MODIFIED_ORIGINAL)
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
