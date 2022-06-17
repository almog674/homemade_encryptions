
# Hexadecimal to binary conversion 
def hex2bin(s): 
	mp = {'0' : "0000", 
		'1' : "0001", 
		'2' : "0010", 
		'3' : "0011", 
		'4' : "0100", 
		'5' : "0101", 
		'6' : "0110", 
		'7' : "0111", 
		'8' : "1000", 
		'9' : "1001", 
		'A' : "1010", 
		'B' : "1011", 
		'C' : "1100", 
		'D' : "1101", 
		'E' : "1110", 
		'F' : "1111" } 
	bin = "" 
	for i in range(len(s)): 
		bin = bin + mp[s[i]] 
	return bin
	
# Binary to hexadecimal conversion 
def bin2hex(s): 
	mp = {"0000" : '0', 
		"0001" : '1', 
		"0010" : '2', 
		"0011" : '3', 
		"0100" : '4', 
		"0101" : '5', 
		"0110" : '6', 
		"0111" : '7', 
		"1000" : '8', 
		"1001" : '9', 
		"1010" : 'A', 
		"1011" : 'B', 
		"1100" : 'C', 
		"1101" : 'D', 
		"1110" : 'E', 
		"1111" : 'F' } 
	hex = "" 
	for i in range(0,len(s),4): 
		ch = "" 
		ch = ch + s[i] 
		ch = ch + s[i + 1] 
		ch = ch + s[i + 2] 
		ch = ch + s[i + 3] 
		hex = hex + mp[ch] 
		
	return hex

# Binary to decimal conversion 
def bin2dec(binary): 	
	binary1 = binary 
	decimal, i, n = 0, 0, 0
	while(binary != 0): 
		dec = binary % 10
		decimal = decimal + dec * pow(2, i) 
		binary = binary // 10
		i += 1
	return decimal 

# Decimal to binary conversion 
def dec2bin(num): 
	res = bin(num).replace("0b", "")
	if(len(res) % 4 != 0): 
		div = len(res) / 4
		div = int(div) 
		counter =(4 * (div + 1)) - len(res) 
		for i in range(0, counter): 
			res = '0' + res 
	return res

def dec_to_bin(x):
    return int(bin(x)[2:])

def dec2hex(x):
    mp = {"0" : '0', 
		"1" : '1', 
		"2" : '2', 
		"3" : '3', 
		"4" : '4', 
		"5" : '5', 
		"6" : '6', 
		"7" : '7', 
		"8" : '8', 
		"9" : '9', 
		"10" : 'A', 
		"11" : 'B', 
		"12" : 'C', 
		"13" : 'D', 
		"14" : 'E', 
		"15" : 'F' } 
    hex_value = ''
    q = ''
    while q != 0:
        q = x // 16
        r = x % 16
        hex_r = mp[str(r)]
        hex_value += str(hex_r)
        x = q
    hex_value = hex_value[::-1]
    return hex_value

def hex2dec(x):
    mp = {"0" : '0', 
		"1" : '1', 
		"2" : '2', 
		"3" : '3', 
		"4" : '4', 
		"5" : '5', 
		"6" : '6', 
		"7" : '7', 
		"8" : '8', 
		"9" : '9', 
		"A" : '10', 
		"B" : '11', 
		"C" : '12', 
		"D" : '13', 
		"E" : '14', 
		"F" : '15' }

    decimal_value = 0
    x = x[::-1]
    for i in range(2):
        decimal_number = mp[x[i]]
        decimal_value += (int(decimal_number) * (16 ** i))
    return str(decimal_value)



def permutation(table, array, n):
    permuted = ''
    for i in range(n):
        permuted = permuted + array[table[i] - 1]
    return permuted

def xor(a, b):
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result = result + '0'
        else:
            result = result + '1'
    return result

def use_pc_one(key, initial_key):
    key_right = ''
    key_left = ''
    for i in pc_one_left:
        key_left = key_left + initial_key[i - 1]
    for i in pc_one_right:
        key_right = key_right + initial_key[i - 1]
    new_key = [key_left, key_right]
    return new_key

def shift_left(key, num):
    new_key = ''
    prev_key = key
    key_range = int(len(key))
    for i in range(0, key_range):
        new_key = new_key + prev_key[(i + num) % key_range]
    return new_key

def use_pc_two(key, pc_two):
    new_key = ''
    for i in range(48):
        new_key = new_key + key[pc_two[i] - 1]
    return new_key


def make_keys(key_list, key_left, key_right):
    for i in range(0, 16):
        if i == 0 or i == 1 or i == 8 or i == 15:
            key_left = shift_left(key_left, 1)
            key_right = shift_left(key_right, 1)
        else:
            key_left = shift_left(key_left, 2)
            key_right = shift_left(key_right, 2)

        full_key = key_left + key_right
        sub_key = use_pc_two(full_key, pc_two)
        key_list.append(sub_key)
        key_show = bin2hex(sub_key)
    return key_list

def initial_permutation(plain_text, table):
    permuted_text = ''
    range_text = len(str(plain_text))
    for i in range(range_text):
        permuted_text = permuted_text + plain_text[table[i] - 1]
    return permuted_text

def divide_text(text):
    left_side = text[: int((len(str(text)) / 2))]
    right_side = text[int((len(str(text)) / 2)):]
    return (str(left_side), str(right_side))

def E_cup(right_side, exp_d):
    extended_text = ''
    for i in range(len(exp_d)):
        extended_text = extended_text + right_side[exp_d[i] - 1]
    return extended_text

def divide_for_sub_table(xored_text):
    parts_list = []
    for i in range(8):
        part = xored_text[(i * 6) : ((i * 6) + 6)]
        parts_list.append(part)
    return parts_list

def use_sbox(parts_list, sbox):
    subtituded = ''
    counter = 0
    for part in parts_list:
        column = part[1 : 5]
        row = part[0] + part[5]
        decimal_row = bin2dec(int(row))
        decimal_column = bin2dec(int(column))
        choosen_table = sbox[counter]
        choosen_row = choosen_table[decimal_row]
        choosen_number = choosen_row[decimal_column]
        # print(choosen_row)
        # print(choosen_number)
        converted_choosen_number = dec_to_bin(choosen_number)
        converted_choosen_number = str(converted_choosen_number).zfill(4)
        subtituded = subtituded + converted_choosen_number
        counter = counter + 1
    return subtituded

        

def f_function(right_side, sub_key):
    extended_text = E_cup(right_side, exp_d)
    xored_text = xor(extended_text, sub_key)
    parts_list = divide_for_sub_table(xored_text)
    parts_subtituded = use_sbox(parts_list, sbox)
    permuted_text = permutation(per, parts_subtituded, 32)
    return permuted_text
            
# Table of Position of 64 bits at initail level: Initial Permutation Table 
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2, 
				60, 52, 44, 36, 28, 20, 12, 4, 
				62, 54, 46, 38, 30, 22, 14, 6, 
				64, 56, 48, 40, 32, 24, 16, 8, 
				57, 49, 41, 33, 25, 17, 9, 1, 
				59, 51, 43, 35, 27, 19, 11, 3, 
				61, 53, 45, 37, 29, 21, 13, 5, 
				63, 55, 47, 39, 31, 23, 15, 7] 

# Expansion D-box Table 
exp_d = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5, 
		6 , 7 , 8 , 9 , 8 , 9 , 10, 11, 
		12, 13, 12, 13, 14, 15, 16, 17, 
		16, 17, 18, 19, 20, 21, 20, 21, 
		22, 23, 24, 25, 24, 25, 26, 27, 
		28, 29, 28, 29, 30, 31, 32, 1 ] 

# Straight Permutaion Table 
per = [ 16, 7, 20, 21, 
		29, 12, 28, 17, 
		1, 15, 23, 26, 
		5, 18, 31, 10, 
		2, 8, 24, 14, 
		32, 27, 3, 9, 
		19, 13, 30, 6, 
		22, 11, 4, 25 ] 

# S-box Table 
sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
		[ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
		[ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]], 
			
		[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], 
			[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], 
			[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], 
		[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]], 
	
		[ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], 
		[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], 
		[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], 
			[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]], 
		
		[ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
		[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], 
		[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], 
			[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ], 
		
		[ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], 
		[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], 
			[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], 
		[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]], 
		
		[ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
		[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
			[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], 
			[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ], 
		
		[ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], 
		[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], 
			[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], 
			[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ], 
		
		[ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
			[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], 
			[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], 
			[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ] 
	
# Final Permutaion Table 
final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32, 
			39, 7, 47, 15, 55, 23, 63, 31, 
			38, 6, 46, 14, 54, 22, 62, 30, 
			37, 5, 45, 13, 53, 21, 61, 29, 
			36, 4, 44, 12, 52, 20, 60, 28, 
			35, 3, 43, 11, 51, 19, 59, 27, 
			34, 2, 42, 10, 50, 18, 58, 26, 
			33, 1, 41, 9, 49, 17, 57, 25 ]

# PC-1 Left
pc_one_left = [57, 49, 41, 33, 25, 17, 9,
               1, 58, 50, 42, 34, 26, 18,
               10, 2, 59, 51, 43, 35, 27,
               19, 11, 3, 60, 52, 44, 36]

# PC-1 Right
pc_one_right = [64, 55, 47, 39, 31, 23, 15,
                7, 62, 54, 46, 38, 30, 22,
                14, 6, 61, 53, 45, 37, 29,
                21, 13, 5, 28, 20, 12, 4]

# PC-2
pc_two = [14, 17, 11, 24, 1, 5, 3, 28,
          15, 6, 21, 10, 23, 19, 12, 4,
          26, 8, 16, 7, 27, 20, 13, 2,
          41, 52, 31, 37, 47, 55, 30, 40,
          51, 45, 33, 48, 44, 49, 39, 56,
          34, 53, 46, 42, 50, 36, 29, 32]

# Key drop 8 bits table
keyp = [57, 49, 41, 33, 25, 17, 9, 
		1, 58, 50, 42, 34, 26, 18, 
		10, 2, 59, 51, 43, 35, 27, 
		19, 11, 3, 60, 52, 44, 36, 
		63, 55, 47, 39, 31, 23, 15, 
		7, 62, 54, 46, 38, 30, 22, 
		14, 6, 61, 53, 45, 37, 29, 
		21, 13, 5, 28, 20, 12, 4 ] 

def make_sub_keys(key):
    initial_key = key
    key = permutation(keyp, key, 56)
    key_left = key[0:28]
    key_right = key[28:56]
    # (key_right, key_left) = use_pc_one(key, initial_key)
    key_list = []
    key_zero = [key_right, key_left]
    key_list = make_keys(key_list, key_left, key_right)
    return key_list

def encrypt(plain_text, sub_keys):
    permuted_text = initial_permutation(plain_text, initial_perm)
    permuted_show = bin2hex(permuted_text)
    print(f'Permuted text: {permuted_show}')
    (left_side, right_side) = divide_text(permuted_text)
    for i in range(16):
        encrypted_right_side = f_function(right_side, sub_keys[i])
        encrypted_right_side = xor(encrypted_right_side, left_side)
        if i == 15:
            left_side = encrypted_right_side
            right_side = right_side
        else:     
            left_side = right_side
            right_side = encrypted_right_side
        right_side_show = bin2hex(str(right_side))
        left_side_show = bin2hex(str(left_side))
        print(f'Round {i}: {left_side_show} {right_side_show} {bin2hex(sub_keys[i])}')
    full_text = left_side + right_side
    cipher_text = permutation(final_perm, full_text, 64)
    hex_cipher_text = bin2hex(cipher_text)
    return hex_cipher_text

def divide_blocks(text, value):
    block_list = []
    starter = 0
    text = text.replace(' ', '')
    while starter != len(text):
        block = text[starter : starter + value]
        block_list.append(block)
        starter += value
    return block_list

def padding(text):
    while len(text) % 8 != 0:
        text = text + '{'
    return text

def convert_text_to_hex(text):
    hex_value = ''
    for letter in text:
        letter_value = ord(letter)
        letter_hex_value = dec2hex(letter_value)
        hex_value += letter_hex_value
    return hex_value

def convert_hex_to_text(hex_value):
    decimal_value = ''
    couple_list = divide_blocks(hex_value, 2)
    for couple in couple_list:
        decimal_couple = hex2dec(couple)
        letter = chr(int(decimal_couple))
        decimal_value += letter
    return decimal_value

        
def main():
    cipher_text = ''
    decrypted_text = ''

    plain_text = 'almog maimon'
    plain_text = padding(plain_text)
    print(f'Plain text: {plain_text}')
    hex_plain_text = convert_text_to_hex(plain_text)
    block_list = divide_blocks(hex_plain_text, 16)
    key =  'AABB09182736CCDD'
    key = hex2bin(key)
    sub_keys = make_sub_keys(key)
    for block in block_list:
        block = hex2bin(block)
        cipher_text = cipher_text + ' ' + encrypt(block, sub_keys)
    print(f'Cipher text: {cipher_text}')
    print('Decryption *********************')
    cipher_block_list = divide_blocks(cipher_text, 16)
    sub_keys.reverse()
    for block in cipher_block_list:
        block = hex2bin(block)
        decrypted_text_hex = encrypt(block, sub_keys)
        decrypted_text_block = convert_hex_to_text(decrypted_text_hex)
        decrypted_text = decrypted_text + decrypted_text_block.replace('{', '')
    print(f'Decrypted text: {decrypted_text}')


if __name__ == "__main__":
    main()