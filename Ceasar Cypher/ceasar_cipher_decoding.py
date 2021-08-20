import alphabets


def decoding(message, number):
    encoded_message = ""

    for letter in message:
        position = alphabets.alphabet.index(letter)
        new_position = position - number
        if new_position<0:
            new_position+=len(alphabets.alphabet)
        encoded_message += alphabets.alphabet[new_position]
    return encoded_message
