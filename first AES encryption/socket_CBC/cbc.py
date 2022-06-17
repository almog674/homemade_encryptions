from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import random

class Encrypt:
    def __init__(self, message, password):
        self.message = message
        self.password = password.encode('utf-8')
        self.mode = AES.MODE_CBC

    def encrypt(self):
        self.IV = self.get_IV()
        self.key = self.make_key(self.password)
        self.padded_message = self.pad_message(self.message)
        self.cipher = AES.new(self.key, self.mode, self.IV)
        self.encrypted_message = self.encrypting_message(self.padded_message, self.cipher)
        return (self.encrypted_message, self.IV)

    def make_key(self, password):
        key = SHA256.new(password).digest()
        return key

    def pad_message(self, message):
        while len(message) % 16 != 0:
            message = message + b'{'
        return message

    def get_IV(self):
        IV = ""
        while len(IV) < 16 :
            number = round(random.randint(0, 9))
            IV = IV + str(number)
        return IV.encode('utf-8')

    def encrypting_message(self, padded_message, cipher):
        encrypted_message = cipher.encrypt(padded_message)
        return encrypted_message

    def decrypt(self, IV):
        self.key = self.make_key(self.password)
        self.cipher = AES.new(self.key, self.mode, IV)
        decrypted_message = self.cipher.decrypt(self.message)
        decrypted_message = decrypted_message.rstrip(b'{')
        return decrypted_message.decode()