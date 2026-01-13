from functools import reduce

data = [1, 2, 3, 4, 5, 6, 2, 4]

even_numbers = filter(lambda x: x % 2 == 0, data)
squared_numbers = map(lambda x: x ** 2, even_numbers)

result = reduce(lambda a, b: a + b, squared_numbers)

print(result)