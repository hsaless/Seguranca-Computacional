def transposition_cipher_decod(cipher_text, key):
    num_rows = len(cipher_text) // len(key)
    tam = len(key)
    dic = {}

    sorted_key = sorted(key)

    for i in range(len(sorted_key)):
        dic[sorted_key[i]] = [i]


    for i in range(len(key)):
        dic[key[i]].append(i)

    
    
    matriz = [[None] * tam for _ in range(num_rows)]

    ind = 0

    for letter, index in dic.items():
        for j in range(len(matriz)):
            matriz[j][index[1]] = cipher_text[ind]
            ind+= 1

    plain_text = ""

    for row in matriz:
        for letter in row:
            plain_text += letter
    
    return plain_text

texto_cifrado = input("Digite o texto cifrado para quebra-lo: ")
chave = input("Digite a chave que foi usada para cifrar: ") 

if(len(texto_cifrado) % len(chave) != 0):
    print("A chave ou o texto foram digitados incorretamente")


elif len(chave) != len(set(chave)):
    print("A chave não pode ter caracteres repetidos")


else:
    print('A mensagem (com caracteres usados para completar a cifra, muito provavelmente representados por "X" é: ' + transposition_cipher_decod(texto_cifrado,chave))





