import alphabets


def encoding(message, number):
    shifted_location = []
    current_location = []
    encoded_message = ""

    input_message_list = list(message)

    for letter in input_message_list:
        current_location.append(alphabets.alphabet.index(letter))
    for shift in current_location:
        shifted_location.append(shift + number)

    for position in shifted_location:
        encoded_message += alphabets.alphabet[position]
    return encoded_message
