numbers = range(1, 21)

even_numbers = filter(lambda x: x % 2 == 0, numbers)

squared_even_numbers = list(map(lambda x: x ** 2, even_numbers))

print(squared_even_numbers)