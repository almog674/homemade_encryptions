import hashlib
text = 'everytime we touch'.encode()
cipher = hashlib.new("md5", text).hexdigest()
print(cipher)