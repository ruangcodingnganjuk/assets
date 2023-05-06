def ganjil_genap(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append("genap")
        else:
            result.append("ganjil")
    return result

# Contoh penggunaan
numbers = [1, 2, 3, 4, 5]
print(ganjil_genap(numbers)) # Output: ['ganjil', 'genap', 'ganjil', 'genap', 'ganjil']
