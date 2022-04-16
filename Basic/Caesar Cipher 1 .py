import switch as switch

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_test = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 26
        new_letter = alphabet[new_position]
        cipher_test += new_letter
    print(f"The encoded text is:  {cipher_test} ")


def decrypt(plain_text, shift_amount):
    cipher_test = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = (position - shift_amount)
        new_letter = alphabet[new_position]
        cipher_test += new_letter
    print(f"The decoded text is:\n {cipher_test} ")


if direction == 'e':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'd':
    decrypt(plain_text=text, shift_amount=shift)
else:
    print("Invalid Choice !!")
