import random

def rabinMiller(n, c):
    # Return true if it's not proven to be not prime
    a = random.randrange(2, (n - 2))
    x = pow(a, int(c), n) # a ^ d mod n
    if (x == 1) or (x == n - 1):
        return True

    while c != (n - 1):
        x = pow(x, 2 , n)
        c * 2

        if x == 1:
            return False
        elif x == n - 1:
            return True
    return False


def isPrime(n):
    # Return True if n is a prime
    # Go to another test in function "rabinMiller" if uncertain
    if n < 2:
        return False

    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    if n in lowPrimes:
        return True

    for prime in lowPrimes:
        if n % prime == 0:
            return False

    # Find number c such that c * 2 ^ r = n - 1
    c = n - 1 # Even because n isn't divisable by two
    while c % 2 == 0:
        c /= 2

    # Prove not prime 128 time
    for i in range(128):
        if not rabinMiller(n, c):
            False

    return True
def generate_keys(keysize = 1024):
    e = d = n = 0

    # Get prime number p and q
    p = generate_large_prime(keysize)
    q = generate_large_prime(keysize)


    n = p * q
    nPI = (q - 1) * (p - 1)

    e = 13
    d = modularInverse(e, nPI)

    # Choose e
    # e has to be relativly prime to phi of n, bigger than 1 and smaller than phi of n.
    while True:
        e = random.randrange(2 ** (keysize - 1),(2 ** keysize) - 1)
        if (is_co_prime(e, nPI)):
            break

    # Choose d
    # d has to be the inverse of e in mod phi of n, e * d (mod nPI) = 1
    d = modularInverse(e, nPI)


    return e, d, n


def generate_large_prime(keysize):
    while True:
        number = random.randrange(2 ** (keysize - 1),(2 ** keysize) - 1)
        print(number)
        if (isPrime(number)):
            return number

def gcd(p, q):
    # The euclidian algorithm to find the gcd of p and q
    que = p // q
    r = (p % q)
    if r == 0:
        return q
    else:
        return gcd(q, r)


def is_co_prime(p, q):
    # Return True if gcd(p, q) is 1
    # Means they are relativly prime

    return gcd(p, q) == 1

def modularInverse(a, b):
    gcd, x, y = gcdExtended(a, b)
    
    if x < 0:
        x + b
    return x


def gcdExtended(a, b):  
    # Base Case  
    if a == 0 :   
        return b,0,1
             
    gcd, x1, y1 = gcdExtended(b%a, a)  
     
    # Update x and y using results of recursive  
    # call  
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y 

def encrypt(e, n, msg):
    cipher = ''
    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, n)) + " "
    return cipher

def decrypt(d, n, cipher_msg):
    msg = ''
    parts = cipher_msg.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, n))
    return msg


def main():
    keysize = 20

    e, d, n = generate_keys(keysize)

    msg = 'Hello World!'
    cipher_text = encrypt(e, n, msg)
    decrypted_text = decrypt(d, n, cipher_text)

    print(f"Message: {decrypted_text}")
    print(f"keys: {d}, {e} Cipher_text: {cipher_text}")
    

main()