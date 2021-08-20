import alphabets


def encoding(message, number):
    encoded_message = ""

    for letter in message:
        position = alphabets.alphabet.index(letter)
        new_position = position + number
        if new_position>len(alphabets.alphabet):
            new_position-=len(alphabets.alphabet)
        encoded_message += alphabets.alphabet[new_position]
    return encoded_message
