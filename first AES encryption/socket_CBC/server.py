import socket
from cbc import Encrypt

IP = '0.0.0.0'
PORT = 44444

class Server:
    def __init__(self, IP, PORT):
        self.PORT = PORT
        self.IP = IP
        self.server = self.initialize_server(self.IP, self.PORT)
        self.client, self.address = self.handle_connection(self.server)
        while True:
            self.handle_client(self.client)

    def initialize_server(self, ip, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((ip, port))
        server.listen()
        print("Server is up and ready!!")
        return server

    def handle_connection(self, server):
        client, address = server.accept()
        print('Client Connected!!')
        return (client, address)

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

    def handle_client(self, client):
        message = client.recv(1024)
        decrypted_message = self.decrypt_message(message)
        response = '[SERVER]: ' + decrypted_message
        encrypt_response = self.encrypt_message(response.encode())
        client.send(encrypt_response)

almog = Server(IP, PORT)