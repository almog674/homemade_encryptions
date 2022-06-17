import math


letter_list = ['a','b','c','d' ,'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k' ,'l' , 'm' , 'n','o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' , 'v', 'w', 'x', 'y', 'z']

def get_input():
    text = input("Put a text to encrypt: ")
    key = input("What is the encryption key: ")
    return (text, key)

def check_squere(key):
    squere = math.sqrt(len(key))
    return (squere - math.floor(squere) == 0)

def check_key(key, squere):
    if (len(key) % 2 != 0) and (squere == False) and (len(key) > 4):
        print('[SYSTEM] invalid key...')
        return False
    else:
        print('[SYSTEM] valid key!!')
        return True

def get_text_value(text):
    split_text = text[:]
    text_value = []
    for char in split_text:
        value = letter_list.index(char)
        text_value.append(value)
    return text_value

def get_matrix(key_value):
    key_matrix = []
    length = math.floor(math.sqrt(len(key_value)))
    # if length < 2:
    #     key_list = key_value
    #     key_matrix.append(key_list)
    #     return (key_matrix, length)
    for part in range(length):
        if part == 0:
            key_list = key_value[0 * length : (1 * length)]
        else:
            key_list = key_value[part * length : (2 * part) * length]
        key_matrix.append(key_list)
    return (key_matrix, length)

def seperate_text(text_value, key_value):
    number = math.ceil(len(text_value) / len(key_value))
    seperated_text = []
    for part in range(number):
        text_list = text_value[part * len(key_value) : (part + 1) * len(key_value)]
        seperated_text.append(text_list)
    return seperated_text

def get_matrix_properties(matrix):
    height = len(matrix)
    return (height, length)



def main():
    valid = True
    while valid != False:
        (text, key) = get_input()
        squere = check_squere(key)
        valid = check_key(key, squere)
        key_value = get_text_value(key)
        text_value = get_text_value(text)
        (key_matrix, length) = get_matrix(key_value)
        seperated_text = seperate_text(text_value, key_value)
        text_3d_matrix = []
        for part in range(len(seperated_text)):
            if len(seperated_text[part]) > 3:
                text_matrix = get_matrix(seperated_text[part])
                print(text_matrix)
                text_heigth, text_length = get_matrix_properties(seperated_text[part])
            print(text_heigth)
            print(text_length)
            # for i in range(len(X)):
            #     # iterate through columns of Y
            #         for j in range(len(Y[0])):
            #             # iterate through rows of Y
            #             for k in range(len(Y)):
            #                 result[i][j] += X[i][k] * Y[k][j]
if __name__ == "__main__":
    main()