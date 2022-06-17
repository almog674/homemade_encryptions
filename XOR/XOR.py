text = input('What do you want to encrypt? ')
key = input('Put an encryption key: ')
text_length = len(text)

cipher = ''

for letter in range(text_length):
    t = text[letter]
    k = key[letter % len(key)]
    cipher_letter = ord(t) ^ ord(k)
    cipher += chr(cipher_letter)
print(cipher.encode("utf-8").hex())