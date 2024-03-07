def contains_string(main_string, sub_string):
    if sub_string in main_string:
        return True
    else:
        return False

main_str = "Hello, how are you?"
sub_str1 = "how"
sub_str2 = "world"

print(contains_string(main_str, sub_str1))  
print(contains_string(main_str, sub_str2))  

#2
def sum_recursive(num):
    if num <= 0:
        return 0
    else:
        return num + sum_recursive(num - 1)

number = 5
result = sum_recursive(number)
print(f"The sum of numbers from 0 to {number} is: {result}")

#3
def reverse_string(s):
    return s[::-1]

original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print("Original:", original_string)
print("Reversed:", reversed_string)

#4 
txt =  ['pandas', 'monkeys', 'koalas', 'kangaroos']
lst = ['fish', 'bird', 'dog', 'cat']
for i in range(len(txt)):
    txt[i] = txt[i].upper()

print(txt)

def cap(lst):
    if len(lst) == 0:
        return []

    return [lst[0].upper()] + cap(lst[1:])
capitalized_lst = cap(lst)
print(capitalized_lst)

#5
def times(lst):
    result = 1
    for x in lst:
        result = result * x
    return result

lst = [4, 3, 5]
print(times(lst))

#6
alphabet = ["a", "b", "a", "c", "b", "d"]
alphabet = list(dict.fromkeys(alphabet))
print(alphabet)