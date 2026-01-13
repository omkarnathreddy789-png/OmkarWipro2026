data = [1, 2, 3, 4, 5, 6, 2, 4]

squared_evens = [x**2 for x in data if x % 2 == 0]

for index, value in enumerate(squared_evens):
    print(index, value)