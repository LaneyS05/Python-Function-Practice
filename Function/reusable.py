def func1(message):
    words = message.split(' ')

    emoji = {
        ":)": "🙂",
        ":(": "🙁",
        ";)": "😉",
        "XD": "😆"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + ' '

    return output


message = input('>')
print(func1(message))
