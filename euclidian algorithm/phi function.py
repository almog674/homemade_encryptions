import math

# ##### Bad way to calculate #####
# def get_input():
#     number = int(input('What is the number? '))
#     return number


# def calculate(big_number, small_number, counter):
#     q = math.floor(big_number / small_number)
#     r = (big_number % small_number)
#     if r == 0:
#         return small_number, r, counter
#     elif r == 1:
#         counter = counter + 1
#         return calculate(small_number, r, counter)
#     else:
#         return calculate(small_number, r, counter)

# def main():
#     number = get_input()
#     counter = 0
#     for i in range(1, number):
#         full_pack = calculate(number, i, counter)
#         counter = full_pack[2]
#     counter = counter + 1
#     print(f'The counter is: {counter}')

# main()

##### Good way to calculate #####
def get_input():
    number = int(input('What is the number? '))
    return number


def main():
    number = get_input()
    counter = 0

main()



