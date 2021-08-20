import ceasar_cipher_decoding
import ceasar_cipher_encoding

action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
message = []
if action == "encode":
    output = ceasar_cipher_encoding.encoding(text,shift)
elif action == "decode":
    output = ceasar_cipher_decoding.decoding(text,shift)
else:
    print("Wrong input")

print(output)
