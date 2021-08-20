from cypher_merged_function import merged_function
from ceasar_art import logo


print(logo)
while 1:
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if action == "encode" or action == "decode":
        output = merged_function(action, text, shift)
        print(output)
    else:
        print("Enter correct input")
    game = input("Please 'N' if you like to exit. Press any other key to continue: ").lower()

    if game == "n":
        print("Have a nice day!")
        break
