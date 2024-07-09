for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

numbers = [1, 1, 1, 1, 5]
for x in numbers:
    if x == 1:
        print('x')
    elif x == 5:
        print('xxxxx')
    else:
        print('not working')


numbers1 = [5, 2, 5, 2, 2]
for x_count in numbers1:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)