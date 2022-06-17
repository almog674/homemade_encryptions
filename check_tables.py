table = [10, 9, 8,
         7, 6, 5,
         4, 3, 2,
         1, 0 ,10]

array_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def permutation(table, array_of_numbers, n):
    permuted_text = ''
    for i in range(n):
        permuted_text = permuted_text + str(array_of_numbers[table[i] - 1])
    print(permuted_text)

permuted_text = permutation(table, array_of_numbers, 12)