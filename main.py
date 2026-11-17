# TODO-1: Import and print the logo from art.py when the program starts.
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if letter.isalpha():
            if encode_or_decode == "decode":
                shifted_position = alphabet.index(letter) - shift_amount
            else:
                shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# TODO-2: What happens if the user enters a number/symbol/space?
should_continue = True

while should_continue:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in ["encode", "decode"]:
            break
        print("Wrong input! Please, try again.")


    text = input("Type your message:\n").lower()

    while True:
        shift_input = (input("Type the shift number:\n"))
        if shift_input.isdigit():
            shift = int(shift_input)
            break
        print("Error! Type a number")

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    while True:
        yes_or_no = input("Would you like to try again?").lower()
        if yes_or_no == "yes":
            break
        elif yes_or_no == "no":
            print("See you later!")
            should_continue = False
            break
        else:
            print("Wrong input! Try again whit 'yes' or 'no'")

# TODO-3: Can you figure out a way to restart the cipher program?
