import math

def get_input():
    big_number = int(input('What is the bigger number? '))
    small_number = int(input('What is the smaller number? '))
    return (big_number, small_number)

def calculate(big_number, small_number, first_big_number, first_small_number):
    q = math.floor(big_number / small_number)
    r = (big_number % small_number)
    if r == 0:
        print(f'The gcd of {first_big_number} and {first_small_number} is {small_number}')
        return
    elif r == 1:
        print("Thw numbers doesn't have a gcd except 1")
        return
    else:
        return calculate(small_number, r, first_big_number, first_small_number)

def main():
    (big_number, small_number) = get_input()
    calculate(big_number, small_number, big_number, small_number)

main()


