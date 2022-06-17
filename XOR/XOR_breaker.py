text = input('What do you want to decrypt? ')
text_length = len(text)

# 5c55504058
# V[ZXP

def get_couples_list(text, text_length):
    couple_list = []
    for part in range(0, text_length, 2):
        couple = text[part : part + 2]
        couple_list.append(couple)
    return couple_list

def convert_to_decimals(couple_list):
    hex_dictionary = {
        '0': 0, '1': 1, '2': 2,
        '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8,
        '9': 9, 'a': 10, 'b': 11,
        'c': 12, 'd': 13, 'e': 14,
        'f': 15
        }
    decimal_list = []
    for couple in couple_list:
        first_charecter_value = int(hex_dictionary[couple[0]])
        secound_charecter_value = int(hex_dictionary[couple[1]])
        number = (first_charecter_value * 16) + secound_charecter_value
        decimal_list.append(number)
    return decimal_list

def convert_to_string(decimal_list):
    converted_string = ''
    for number in decimal_list:
        character = chr(number)
        converted_string = converted_string + character
    string_length = len(converted_string)
    print(converted_string)
    return (converted_string, string_length)

def main():
    couple_list = get_couples_list(text, text_length)
    decimal_list = convert_to_decimals(couple_list)
    (converted_string, string_length) = convert_to_string(decimal_list)
    (clear, key) = decrypt_text(converted_string, string_length)

def add_padding(key, guess):
    guess = str(guess)
    guess = guess.zfill(int(key))
    return guess

def execute_key(key, text, text_length):
    decipher_text = ''
    for letter in range(text_length):
        t = text[letter]
        k = key[letter % len(key)]
        decipher_number = ord(t) ^ ord(k)
        decipher_character = chr(decipher_number)
        decipher_text = decipher_text + decipher_character
    return decipher_text

def write_document(decipher_text, padded_key):
    password_table = open(r"C:\Users\97254\Desktop\cyber\learning python\encryption\ceaser cipher\XOR\password_table", "a")
    password_table.write(f"Decrypted: {decipher_text} | Password: {padded_key} \r\n")

    


def decrypt_text(text, text_length):
    key = input('How many digits the key has? ')
    if int(key) > 3:
        print('You cannot choose a key with more than 4 digits... ')
        key = input('How many digits the key has? ')
    guess_range = 10 ** int(key)
    password_table = open(r"C:\Users\97254\Desktop\cyber\learning python\encryption\ceaser cipher\XOR\password_table", "w")
    password_table.write("")
    for guess in range(guess_range):
        padded_key = add_padding(key, guess)
        decipher_text = execute_key(padded_key, text, text_length)
        write_document(decipher_text, padded_key)
    return 1, 2
    # for number_one in '0123456789':
    #     for number_two in '0123456789':
    #         number = number_one + number_two
    #         clear = ''
    #         for letter in range(text_length):
    #             t = text[letter]
    #             decipher_letter = ord(t) ^ ord(number)
    #             character = chr(decipher_letter)
    #             clear = clear + character
    #         print(clear, number)
    # return (clear, number)


if __name__ == '__main__':
    main()
    
