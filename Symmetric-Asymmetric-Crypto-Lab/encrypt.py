import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
from cryptography.hazmat.backends import default_backend

# Encrypt Function: Encrypts the plaintext using AES-128 bit in CBC mode with PKCS7 padding
def encrypt(plaintext, key, iv):
  

    # AES only works with 16 bytes since 128-bit
    # The plaintext isn't exactly 16 byte therefore PKCS7 is added to help with the bytes
    padder_input = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_output = padder_input.update(plaintext.encode()) + padder_input.finalize()

    # Creating AES Cipher in CBC mode with key and IV that is generated in main
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Storing the result of encryptor with padded output in encrypt_text
    encrypt_text = encryptor.update(padded_output) + encryptor.finalize()

    # Converting the encrypt_text to Base64 format and return the encrypt_text
    return base64.b64encode(encrypt_text).decode()



# Decrypt Function: Decrypts the AES-128 bit (CBC) encrypted in base64 format and removes padding
def decrypt(encrypted_base64, key, iv):
 
    # Converting encrypt base64 version back to the original encrypt text before base64 format
    original_encrypt = base64.b64decode(encrypted_base64)

    # Creating AES Cipher for decryption
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypting the original_encrypt
    decrypted_padder= decryptor.update(original_encrypt) + decryptor.finalize()

    # Removing padding to get back the original plaintext
    removed_padder = padding.PKCS7(algorithms.AES.block_size).unpadder()

    decrypted = removed_padder.update(decrypted_padder) + removed_padder.finalize()

    # Returning the decrypted
    return decrypted.decode()


    

# Main Function: 

def main():
   
    # Initializing plaintext 
    plaintext = "Syeda Chowdhury" 

 
    print("Plaintext string:", plaintext) # Output 1

    # Creating a random 128-bit AES key and IV value
    key = os.urandom(16)  
    iv = os.urandom(16)   

    # Encrypting plaintext by storing the result in encrypted from function encrypt which passes in plaintext, key and iv as parameters and returns encrypted text in base64 format
    encrypted = encrypt(plaintext, key, iv)


    print("Encrypted valued in BASE64 format: ", encrypted) # Output 2

    # Decrypting the encrypted by storing the result in decrypted from function decrypt which passes in encrypted_base64, key and iv as parameters and returns decypted text 
    decrypted = decrypt(encrypted, key, iv)

    print("Decrypted string:", decrypted) # Output 3


if __name__ == "__main__":
    main()
