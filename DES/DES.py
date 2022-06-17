from Crypto.Cipher import DES
from secrets import token_bytes

# Get 8 bytes random key
key = token_bytes(8)

def encrypt(message):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    cipher_text, tag = cipher.encrypt_and_digest(message.encode('ascii'))
    return (nonce, cipher_text, tag)

def decrypt(nonce, cipher_text, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce = nonce)
    plain_text = cipher.decrypt(cipher_text)

    try:
        cipher.verify(tag)
        return plain_text.decode('ascii')
    except:
        return False

nonce, cipher_text, tag = encrypt(input('What do you want to encrypt? '))
plain_text = decrypt(nonce, cipher_text, tag)

print(f'Cipher text: {cipher_text}')

if not plain_text:
    print('The message is corrupted!')
else:
    print(f"Plain text: {plain_text}")

