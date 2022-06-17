import socket
from cbc import Encrypt

IP = '127.0.0.1'
PORT = 44444

class Client:
    def __init__(self, IP, PORT):
        self.PORT = PORT
        self.IP = IP
        self.client = self.initialize_client(self.IP, self.PORT)
        while True:
            # try:
            message = input('What do you want to send for the server? ')
            cipher_message = self.encrypt_message(message.encode())
            self.send_message(self.client, cipher_message)
            response = self.get_response(self.client)
            decrypted_response = self.decrypt_message(response)
            print(decrypted_response)
            # except:
            #     print('Something went wrong...')
            #     break

    def initialize_client(self, ip, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        return client

    def encrypt_message(self, message):
        encryption = Encrypt(message, 'almog674')
        cipher_message, IV = encryption.encrypt()
        cipher_message = cipher_message + IV
        return cipher_message

    def decrypt_message(self, response):
        IV = response[len(response) - 16 : len(response)]
        response = response[0: len(response) - 16]
        decrypted = Encrypt(response, 'almog674')
        decrypted_response = decrypted.decrypt(IV)
        return decrypted_response

    def send_message(self, client, cipher_message):
        client.send(cipher_message)

    def get_response(self, client):
        response = client.recv(1024)
        return response
        


almog = Client(IP, PORT)