alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypted_text = []
output_text = ""
# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    if direction == "encode":
        for letter in original_text:
            acc_index = alphabet.index(letter)
           # print(acc_index)
            acc_index += shift_amount
            acc_index = acc_index % len(alphabet)
            encrypted_text.append(alphabet[acc_index])

            #dummy_content = ''.join(encrypted_text)
        print("Your encoded text is: " + ''.join(encrypted_text))

encrypt(text, shift)



# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

