customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jean Smith"
print(customer.get("name"))

phone = input('Phone: ')
digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}
output = ''
for num in phone:
    output += digits.get(num, "!") + ' '
print(output)

message = input('>')
words = message.split(' ')

emoji = {
    ":)": "🙂",
    ":(": "🙁",
    ";)": "😉",
    "XD": "😆"
}
output = ''
for word in words:
    output += emoji.get(word, word) + ' '
print(output)