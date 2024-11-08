def shift_cipher(text, k = 3):
    cipher_text = ""
    for letter in text:
        if letter.isalpha():
            if letter.islower():
                base = ord("a")
                substitute = (((ord(letter) - base) + k) % 26) + base
                cipher_text += chr(substitute)
            else:
                base = ord("A")
                substitute = (((ord(letter) - base) + k) % 26) + base
                cipher_text += chr(substitute)

        else:
            cipher_text += letter
    return cipher_text

message = input("Digite a mensagem a ser cifrada: ")
key = int(input(f"Digite a chave que será usada para cifrar a mensagem: {message} "))

print(shift_cipher(message, key))

