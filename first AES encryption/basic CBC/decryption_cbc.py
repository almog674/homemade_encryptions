from Crypto.Cipher import AES
from Crypto.Hash import SHA256

password = b'almog674'
key = SHA256.new(password).digest()
mode = AES.MODE_CBC
IV = '0123456789ABCDEF'.encode('UTF-8')

cipher = AES.new(key, mode, IV)

with open('basic CBC\encrypted_file', 'rb') as e:
    encrypted_file = e.read()

decrypted_file = cipher.decrypt(encrypted_file)

with open("basic CBC\decrypted_excel.xlsx", 'wb') as df:
    df.write(decrypted_file.rstrip(b'{'))

