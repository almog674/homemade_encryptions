def get_input():
    text = input("Put a text to encrypt: ")
    key = input("What is the encryption key: ")
    return (text, key)

def change_position(text, key):
    char_array = text[:]
    cipher_text = ''
    for char in char_array:
        char_ord = (ord(char) - 97)
        formula = (char_ord + int(key)) % 26
        char = chr(formula + 97)
        cipher_text = cipher_text + char
    return cipher_text

def main():
    (text, key) = get_input()
    chipher_text = change_position(text, key)
    print(chipher_text)


if __name__ == "__main__":
    main()