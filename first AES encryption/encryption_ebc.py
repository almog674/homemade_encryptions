from Crypto.Cipher import AES
from Crypto.Hash import SHA256

password = input("Enter Password: ")
hash_obj = SHA256.new(password.encode('UTF-8'))
hash_key = hash_obj.digest()
PAD = "{"
BLOCK_SIZE = 16

def encrypt(info):
    msg = info
    padding = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PAD
    cipher = AES.new(hash_key, AES.MODE_ECB)
    result = cipher.encrypt(padding(msg).encode('UTF-8'))
    return result

def decrypt(info):
    msg = info
    decipher = AES.new(hash_key, AES.MODE_ECB)
    pt = decipher.decrypt(msg).decode('utf-8')
    pad_index = pt.find(PAD)
    result = pt[:pad_index]
    return result

cipher_text = encrypt(password)
decipher_text = decrypt(cipher_text)
print(cipher_text)
print(decipher_text)