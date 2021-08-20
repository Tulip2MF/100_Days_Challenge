from alphabets import alphabet


def merged_function(action, message, number):
    new_position = ""
    output_message = ""
    number = number % len(alphabet)
    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            if action == "encode":
                new_position = position + number
                if new_position > (len(alphabet)-1):
                    new_position -= len(alphabet)
            else:
                new_position = position - number
                if new_position < 0:
                    new_position += len(alphabet)
            output_message += alphabet[new_position]
        else:
            output_message += letter

    return output_message
