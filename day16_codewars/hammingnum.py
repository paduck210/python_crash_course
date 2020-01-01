def hamming(n):
    hamming_numbers = [1]
    i2, i3, i5 = 0, 0, 0

    while True:
        if len(hamming_numbers) == n:
            return hamming_numbers[-1]

        n2 = 2 * hamming_numbers[i2]
        n3 = 3 * hamming_numbers[i3]
        n5 = 5 * hamming_numbers[i5]

        next_number = min([n2, n3, n5])

        if n2 == next_number:
            i2 += 1
        if n3 == next_number:
            i3 += 1
        if n5 == next_number:
            i5 += 1

        hamming_numbers.append(next_number)

print(hamming(100))