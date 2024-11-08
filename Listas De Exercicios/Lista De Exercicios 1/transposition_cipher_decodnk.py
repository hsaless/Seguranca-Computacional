from itertools import permutations

def transposition_cipher_decod(cipher_text):
    max_key_length = 26
    possible_plaintexts = []

    
    for key_length in range(1, max_key_length + 1):
        if len(cipher_text) % key_length != 0:
            continue  
        
        num_rows = len(cipher_text) // key_length
        matriz = [[None] * key_length for _ in range(num_rows)]
        
        
        for perm in permutations(range(key_length)):
            dic = {}
            for i in range(key_length):
                dic[perm[i]] = i
            
            ind = 0
            
            for coluna in range(key_length):
                for linha in range(num_rows):
                    matriz[linha][dic[coluna]] = cipher_text[ind]
                    ind += 1

            
            plain_text = ""
            for row in matriz:
                for letter in row:
                    plain_text += letter

            possible_plaintexts.append((plain_text, perm))

    return possible_plaintexts


cipher_text = input("Digite o texto cifrado para quebra-lo: ")
decoded_texts = transposition_cipher_decod(cipher_text)


for text, key in decoded_texts:
    print(f"A Chave: {key} gera o Texto Decifrado: {text}")
