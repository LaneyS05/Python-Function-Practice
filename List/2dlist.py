matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

my_num = [1, 1, 2, 3, 4, 5, 6, 6, 7, 7,]
my_num = list(dict.fromkeys(my_num))
print(my_num)

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)