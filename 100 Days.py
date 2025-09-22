#Day 8 - Caesar Cipher

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Enter text to encrypt: ")
shift = int(input("Enter shift number: "))



def caesar(original_text, shift_amount, encode_or_decode):
    result_text = ""
    # This "if" statement handles decoding by reversing the shift direction
    if encode_or_decode == "decode":
        #Shift amount = -1 is the same as shift_amount = shift_amount * -1, which reverses the shift direction
        shift_amount *= -1
    # This for loop goes through each letter in the original text
    for letter in original_text:
        # We create a new variable to hold the shifted position of the letter
        shifted_position = alphabet.index(letter) + shift_amount
        # Modulo operator ensures that the shifted position wraps around the alphabet
        shifted_position %= len(alphabet)
        result_text += alphabet[shifted_position]

    print(f"Here's the encoded result: {result_text}")

caesar(original_text = text, shift_amount = shift, encode_or_decode = direction)