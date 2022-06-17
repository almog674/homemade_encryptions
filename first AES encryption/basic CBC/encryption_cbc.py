from Crypto.Cipher import AES
from Crypto.Hash import SHA256

password = b'almog674'
key = SHA256.new(password).digest()
mode = AES.MODE_CBC
IV = '0123456789ABCDEF'.encode('UTF-8')

def pad_message(message):
    while len(message) % 16 != 0:
        message = message + b"{"
    return message

cipher = AES.new(key, mode, IV)

# text = "I walking on the same street, and it's looking like it looks everyday"
# padded_text = pad_message(text)
# print(padded_text)

with open('basic CBC\my_secret_message.xlsx', 'rb') as f:
    orig_file = f.read()

padded_file = pad_message(orig_file)

encrypted_message = cipher.encrypt(padded_file)

with open('basic CBC\encrypted_file', 'wb') as e:
    e.write(encrypted_message)