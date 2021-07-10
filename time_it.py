from time import time
from aesjosephus import encrypt, decrypt

def record_time(func):
    start_time = time()
    func()
    return time()-start_time

def main():
    n = 100
    encrypt_normal_time = sum(record_time(lambda: encrypt("abcdefghijklmnop","abcdefghijklmnop",mode="normal")) for n in range(n))/n
    encrypt_josephus_time = sum(record_time(lambda: encrypt("abcdefghijklmnop","abcdefghijklmnop",mode="josephus")) for n in range(n))/n
    encrypt_modified_aes_time = sum(record_time(lambda: encrypt("abcdefghijklmnop","abcdefghijklmnop",mode="modified")) for n in range(n))/n
    decrypt_normal_time = sum(record_time(lambda: decrypt("abcdefghijklmnop","abcdefghijklmnop",mode="normal")) for n in range(n))/n
    decrypt_josephus_time = sum(record_time(lambda: decrypt("abcdefghijklmnop","abcdefghijklmnop",mode="josephus")) for n in range(n))/n
    decrypt_modified_aes_time = sum(record_time(lambda: decrypt("abcdefghijklmnop","abcdefghijklmnop",mode="modified")) for n in range(n))/n
    print(f"""
    n = {n}
    Normal AES encryption time used: {encrypt_normal_time:.3e}s / {encrypt_normal_time}s 
    Josephus AES encryption time used: {encrypt_josephus_time:.3e}s / {encrypt_josephus_time}s
    Modified AES encryption time used: {encrypt_modified_aes_time:.3e}s / {encrypt_modified_aes_time}s
    Normal AES decryption time used: {decrypt_normal_time:.3e}s / {decrypt_normal_time}s
    Josephus AES decryption time used: {decrypt_josephus_time:.3e}s / {decrypt_josephus_time}s
    Modified AES decryption time used: {decrypt_modified_aes_time:.3e}s / {decrypt_modified_aes_time}s
    """
    )

if __name__=="__main__":
    main()
