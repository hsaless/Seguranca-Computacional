def shift_cipher_decodbf(cipher_text):
    possible_plaintexts = []

    for k in range(26):
        plain_text = ""
        for letra in cipher_text:
            if letra.isalpha():
                if letra.islower():
                    base = ord("a")
                    substituto = (((ord(letra) - base) - k) % 26) + base
                    plain_text += chr(substituto)
                else:
                    base = ord("A")
                    substituto = (((ord(letra) - base) - k) % 26) + base
                    plain_text += chr(substituto)
            else:
                plain_text += letra

        possible_plaintexts.append((plain_text, k))
    
    return possible_plaintexts

message = input("Digite o texto cifrado para ser quebrado em todas as possíveis mensagens: ")
print(shift_cipher_decodbf(message))



